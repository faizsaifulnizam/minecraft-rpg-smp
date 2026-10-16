"""Check the public source tree without launching Minecraft or using a network."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md', '.html', '.json', '.py', '.yml', '.yaml', '.toml', '.txt', '.css', '.svg', ''}
FORBIDDEN_PARTS = {'saves', 'logs', 'backups', 'crash-reports', 'recordings', 'node_modules', '.venv'}
PRIVATE_PATTERNS = {
    'machine-specific Windows path': re.compile(r'(?i)\b[a-z]:[\\/]'),
    'machine-specific Unix home': re.compile(r'/(?:home|Users)/[A-Za-z0-9_.-]+/'),
    'private IPv4 address': re.compile(r'\b(?:192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b'),
    'GitHub credential pattern': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b'),
    'private key material': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
}

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.active_content = False
    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'iframe', 'object', 'embed'}:
            self.active_content = True
        for name, value in attrs:
            if name in {'href', 'src'} and value:
                self.targets.append(value)
            if name.lower().startswith('on'):
                self.active_content = True

def check(root: Path) -> tuple[int, list[str]]:
    errors = []
    count = 0
    root = root.resolve()
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if '.git' in rel.parts or '__pycache__' in rel.parts:
            continue
        if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
            errors.append(f'{rel}: links/junctions are not permitted')
            continue
        if path.is_dir():
            continue
        if any(part.lower() in FORBIDDEN_PARTS for part in rel.parts):
            errors.append(f'{rel}: private/generated directory')
        if path.suffix.lower() not in TEXT_SUFFIXES or path.name.startswith('.env'):
            errors.append(f'{rel}: file type not approved for public source')
            continue
        if path.stat().st_size > 2_000_000:
            errors.append(f'{rel}: exceeds source-file review budget')
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeError:
            errors.append(f'{rel}: not UTF-8 source')
            continue
        count += 1
        for label, pattern in PRIVATE_PATTERNS.items():
            if pattern.search(text):
                errors.append(f'{rel}: {label}')
        links = []
        if path.suffix == '.md':
            links = re.findall(r'!?\[[^\]\n]*\]\(([^)\s]+)(?:\s+[^)]*)?\)', text)
        elif path.suffix in {'.html', '.svg'}:
            parser = Links()
            parser.feed(text)
            links = parser.targets
            if parser.active_content:
                errors.append(f'{rel}: active HTML content')
        for target in links:
            parsed = urlsplit(target)
            if parsed.scheme:
                if parsed.scheme not in {'http', 'https', 'mailto', 'data'}:
                    errors.append(f'{rel}: unsupported link scheme')
                continue
            if parsed.netloc or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root) or not dest.is_file():
                errors.append(f'{rel}: broken/outside relative link {parsed.path}')
    if not count:
        errors.append('no public source files checked')
    return count, errors

def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        a = root / 'README.md'
        a.write_text('# Example\n[Guide](guide.md)\n', encoding='utf-8')
        (root / 'guide.md').write_text('# Guide\n', encoding='utf-8')
        if check(root)[1]:
            raise RuntimeError('valid tree rejected')
        a.write_text('[Missing](missing.md)', encoding='utf-8')
        if not any('relative link' in e for e in check(root)[1]):
            raise RuntimeError('missing-link control accepted')
        a.write_text('C' + chr(58) + '/' + 'Users' + '/' + 'Example/private', encoding='utf-8')
        if not any('Windows path' in e for e in check(root)[1]):
            raise RuntimeError('private-path control accepted')
        a.write_text('# Safe', encoding='utf-8')
        (root / 'unapproved.jar').write_bytes(b'not an actual mod')
        if not any('file type' in e for e in check(root)[1]):
            raise RuntimeError('binary-file control accepted')
    print('PASS: public-tree checker valid case and three invalid controls')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--self-test', action='store_true')
    args = ap.parse_args()
    if args.self_test:
        self_test()
    else:
        count, errors = check(ROOT)
        for error in errors:
            print('FAIL:', error)
        print(f'{count} UTF-8 source files checked; {len(errors)} issues')
        raise SystemExit(1 if errors else 0)
