"""Offline catalogue validation and optional read-only local mod verification (Python 3.11+)."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / 'modpack/modpack.lock.json'


def validate(data):
    errors = []
    if data.get('schema_version') != 1 or data.get('minecraft') != '1.21.1' or data.get('neoforge') != '21.1.250':
        errors.append('Unsupported schema or target')
    rows = data.get('files', [])
    if not rows:
        errors.append('Empty catalogue')
    seen = set()
    for row in rows:
        name = row.get('filename', '')
        if not name or '/' in name or '\\' in name or ':' in name or name in ('.', '..') or name in seen:
            errors.append('Unsafe or duplicate filename: ' + name)
        seen.add(name)
        state = row.get('state')
        if state not in ('active', 'disabled') or not name.endswith('.jar' if state == 'active' else '.jar.disabled'):
            errors.append('Invalid archive state: ' + name)
        if type(row.get('size')) is not int or row['size'] <= 0:
            errors.append('Invalid size: ' + name)
        for algo, length in [('sha1', 40), ('sha256', 64), ('sha512', 128)]:
            if not re.fullmatch('[0-9a-f]{' + str(length) + '}', row.get('hashes', {}).get(algo, '')):
                errors.append('Invalid ' + algo + ': ' + name)
        origin = row.get('origin')
        if origin:
            url = urlsplit(origin.get('url', ''))
            if url.scheme != 'https' or url.hostname != 'cdn.modrinth.com' or url.username or url.password or url.query or url.fragment or not url.path.startswith('/data/'):
                errors.append('Untrusted download URL: ' + name)
            if origin.get('provider') != 'modrinth' or not origin.get('version_id') or not origin.get('project_id'):
                errors.append('Missing public release identity: ' + name)
            if origin.get('size') != row.get('size') or any(origin.get('hashes', {}).get(a) != row.get('hashes', {}).get(a) for a in ('sha1', 'sha512')):
                errors.append('Publisher hash/size mismatch: ' + name)
        elif not row.get('manual_reason'):
            errors.append('Unexplained manual prerequisite: ' + name)
    counts = {s: sum(r.get('state') == s for r in rows) for s in ('active', 'disabled')}
    if counts != data.get('counts'):
        errors.append('Count mismatch')
    return errors


def check_directory(data, directory):
    """directory is the mods folder itself; never executes or imports its contents."""
    errors = []
    expected = {r['filename'] for r in data['files']}
    actual = {p.name for p in directory.iterdir() if p.name.endswith(('.jar', '.jar.disabled'))}
    errors.extend('Unexpected archive: ' + n for n in sorted(actual - expected))
    for row in data['files']:
        path = directory / row['filename']
        if path.is_symlink() or not path.is_file():
            errors.append('Missing/nonregular archive: ' + row['filename'])
            continue
        if path.stat().st_size != row['size']:
            errors.append('Size mismatch: ' + row['filename'])
            continue
        digests = {a: hashlib.new(a) for a in row['hashes']}
        with path.open('rb') as handle:
            for chunk in iter(lambda: handle.read(1048576), b''):
                for digest in digests.values():
                    digest.update(chunk)
        if any(d.hexdigest() != row['hashes'][a] for a, d in digests.items()):
            errors.append('Hash mismatch: ' + row['filename'])
    return errors


def self_test():
    payload = b'offline synthetic bytes, not a mod'
    row = dict(filename='synthetic.jar', state='active', size=len(payload), hashes={a: hashlib.new(a, payload).hexdigest() for a in ('sha1', 'sha256', 'sha512')}, origin=None, manual_reason='Synthetic test only')
    data = dict(schema_version=1, minecraft='1.21.1', neoforge='21.1.250', counts={'active': 1, 'disabled': 0}, files=[row])
    assert not validate(data)
    for key, value in [('filename', '../escape.jar'), ('size', -1), ('state', 'future')]:
        bad = copy.deepcopy(data); bad['files'][0][key] = value
        assert validate(bad), key
    bad = copy.deepcopy(data); bad['files'].append(copy.deepcopy(row))
    assert validate(bad)
    for url in ('http://cdn.modrinth.com/data/x', 'https://evil.example/data/x', 'https://cdn.modrinth.com@evil.example/data/x'):
        bad = copy.deepcopy(data); bad['files'][0]['origin'] = {'url': url}
        assert validate(bad)
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp); (folder / row['filename']).write_bytes(payload)
        assert not check_directory(data, folder)
        (folder / row['filename']).write_bytes(b'x' * len(payload))
        assert check_directory(data, folder)
    print('PASS: offline self-test, malformed records, URL guards and byte-tamper rejection')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--directory', type=Path, help='Explicit mods directory to verify read-only')
    args = parser.parse_args()
    if args.self_test:
        self_test(); return 0
    data = json.loads(LOCK.read_text(encoding='utf-8'))
    errors = validate(data)
    if args.directory and not errors:
        errors.extend(check_directory(data, args.directory))
    if errors:
        print('\n'.join(errors)); return 1
    print('PASS: catalogue integrity; active={active}, disabled={disabled}'.format(**data['counts']))
    print('Manual origins:', sum(not r['origin'] for r in data['files']))
    print('Not a runtime, permission, dependency-closure or complete-export certification.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
