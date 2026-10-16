# Developmental modpack source

Author: Muhammad Faiz Saifulnizam. Target: Minecraft **1.21.1**, NeoForge **21.1.250**, Java 21.

**Not a complete one-click modpack.** No `.mrpack` is supplied. This is an immutable, hash-locked developmental snapshot: **139 active archives and 2 disabled archives**. These are archive counts, not declared mod-ID counts. Main-instance and historical pack counts are not this snapshot. Recommendations are future work, not installed content.

## What is here

- [Readable archive catalogue](MODLIST.md): exact filenames, active/disabled state and verified upstream release links.
- `modpack.lock.json`: full catalogue and lock in one file; exact local size, SHA-1, SHA-256 and SHA-512, active/disabled state, and public release metadata where proven.
- 123 exact SHA-512 matches were checked against Modrinth batch version_files, official individual release details, and project metadata. URLs and sizes describe those exact publisher files; hosting availability and runtime compatibility are not guaranteed.
- `overrides/config/mca.json`: newly authored minimal allowlisted schema-2 preset from the verified existing schema. Villager chat AI/tools are off; tokens are empty. No full configuration or secrets are copied. Effective runtime uptake has not been tested.
- No third-party JARs, resource packs, shaders, fetched source code, worlds, accounts, maps, logs or launcher credentials are included. Upstream licence metadata is informational, not a new licence grant. Local original or patched mods are not distributed by this source export.

## Manual reconstruction (private, isolated instance only)

1. Install Java 21 and Prism Launcher through their official distribution channels. Create a **new** Minecraft 1.21.1 / NeoForge 21.1.250 instance. Do not overwrite a working instance or load an existing world.
2. Read every `files` record in the lock. For records with `origin`, use its exact official `release_url` and `url`, checking the original publisher terms. Download manually; these scripts perform no network requests. Preserve the local `filename` even when the upstream filename differs.
3. For `origin: null`, stop until you have an authorized exact copy. There is no verified public download in this export. Receipt leads, when present, are historical hints only, not verified current public origins. Compare all hashes and size; never replace a local repair, custom build or unknown JAR with a same-named release. If no authorized exact copy exists, exact reconstruction is blocked.
4. Put active entries under the new instance `minecraft/mods/`. Disabled entries retain the literal `.jar.disabled` suffix. They are historical inventory, not enabled recommendations. The optional directory verifier checks both populations for exact archival reconstruction.
5. Copy only `overrides/config/mca.json` to the new instance `minecraft/config/mca.json` while stopped. Do not copy private global configuration, server settings or diagnostic JVM agents. Other historical settings are not reproduced here.
6. From the repository root, run the offline checks below. `--directory` takes the **mods directory itself**. A passing check establishes bytes/catalogue agreement only; it does not establish rights, dependency compatibility or gameplay safety.
7. Only after all manual gates and exclusions are understood, perform your own approved clean-instance startup and disposable-world tests: loading, gameplay, save/reopen and multiplayer. No such tests were run for this export. Do not use valuable saves.

```text
python scripts/verify_modpack.py --self-test
python scripts/verify_modpack.py
python scripts/verify_modpack.py --directory "YOUR_NEW_INSTANCE/minecraft/mods"
python scripts/check_export_ready.py
```

The export-readiness check intentionally exits nonzero with every missing active-origin record and asset/configuration/rights gates; it creates no archive. It is a blocker report, not a pack builder. Offline catalogue validation may pass while export is correctly blocked.

## Manual / unresolved origins

| Exact archive | State | Requirement |
|---|---|---|
| `aco1.5.33_1.21.1.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `celerium-0.3.1-beta-neoforge-1.21.1-.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `citresewn-neoforge-1.21.1-0.jar.disabled` | disabled | Authorized exact bytes; verify lock hashes/size. |
| `dungeons-and-taverns-v4.4.4.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `foxablazeaqzl_wiki-1.0.2.3.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `framegen-1.3-neoforge-1.21.1.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `ftb-chunks-neoforge-2101.1.22.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `ftb-library-neoforge-2101.1.37.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `ftb-teams-neoforge-2101.1.10.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `hadal-depths-neoforge-1.21.1-2.2.0.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `irons_spellbooks-1.21.1-3.16.3.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `SLR1.3.3.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `staffrepair-0.1.1-dev.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `tensura-neoforge-2.0.1.3.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `tensura_boss_structure-1.0.3.3.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `tensura_trepu-1.0.0.2.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `tensuraleveling-1.0.14.jar` | active | Authorized exact bytes; verify lock hashes/size. |
| `twilightforest-1.21.1-4.8.3345-universal.jar` | active | Authorized exact bytes; verify lock hashes/size. |

## Asset and behavior limits

The local resource-pack stack includes external visual packs and patched assets. None is redistributed. Historical receipt evidence identifies Fresh Animations: Player Extension, Icon Xaero’s, VanillaTweaks and other local visual assets; it does not establish a complete current public asset lock. Base Fresh Animations is not silently added. Shaders and their overrides are excluded.

Known local repair-asset families include SLR Beru-vector recovery, SLR Necromancer rest-pose fallback, Ars unused swim/charge animation repair, and Tensura warp-pad parent repair. These are **reconstruction blockers**, not bundled fixes or permission to republish upstream assets. Obtain authorized originals and separately review exact patch rights/procedure; no synthesized download or replacement is provided.

Consequently the locked archive set plus AI-off preset is a verifiable partial reconstruction path, **not exact reproduction of the owner’s full visual/configuration behavior**. Additional authorized manual prerequisites and runtime acceptance remain open. A future complete release requires a newly reviewed manifest; removing an unknown mod changes the snapshot and cannot be represented as this pack.
