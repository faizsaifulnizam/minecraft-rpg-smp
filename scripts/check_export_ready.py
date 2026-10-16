"""Fail-closed exact-export gate. Never downloads or packages third-party bytes."""
import json
from verify_modpack import LOCK, validate


def blockers(data):
    errors = validate(data)
    errors.extend('Manual origin: ' + r['filename'] for r in data['files'] if r['state'] == 'active' and not r['origin'])
    errors.extend(data.get('reconstruction_blockers', []))
    # This developmental snapshot has no approved complete-export permission/config manifest.
    # Do not remove this gate just because every binary acquires a hosting URL.
    errors.append('Complete export is not approved: exact configuration, asset/patch prerequisites and distribution rights require a new reviewed release manifest.')
    return errors


def main():
    data = json.loads(LOCK.read_text(encoding='utf-8'))
    errors = blockers(data)
    print('REFUSED: no .mrpack written. This is developmental source, not a complete one-click pack.')
    print('\n'.join('- ' + error for error in errors))
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
