# Contributing

Start with the [server plan](docs/server-plan.md), [roadmap](docs/roadmap.md) and [modpack guide](modpack/README.md), so changes address the intended player experience.

## Small, checkable changes

1. Open an issue describing the player outcome, the current gap and the smallest proposed change.
2. Keep the change focused. Prefer supported configuration or upstream fixes before custom replacements.
3. Include evidence: exact versions, public sources, the check you ran and what remains untested.

Use Python 3.11 or newer for the repository scripts. Run these commands from the repository root before a pull request:

```sh
python scripts/verify_modpack.py --self-test
python scripts/verify_modpack.py
python scripts/check_public.py
```

Use the standard library unless a demonstrated need justifies another dependency. A new gameplay implementation needs its own test contract; passing these repository checks does not prove Minecraft integration.

## Keep these distinctions clear

- A selected mod is not an installed mod.
- An installed file is not proof that the game loaded it.
- A successful startup is not gameplay, multiplayer or save/reopen acceptance.
- A source-level idea is not an exact binary match or permission to copy code.
- A performance hypothesis is not a measured improvement.

Do not upload accounts, worlds, server lists, raw logs, diagnostic recordings, tokens, local absolute paths or third-party binaries/assets. Use sanitized, minimal reproductions and official source links instead. Do not change access, flight, money, death or party rules without updating the acceptance requirements.

Contributions do not authorize publication of someone else’s work. Confirm applicable rights and ask the owner before adding substantial third-party material. Keep discussions practical and respectful. Do not report secrets or exploitable details in public issues; see [SECURITY.md](SECURITY.md).
