# Minecraft RPG SMP

A development modpack and server-design project for Minecraft Java 1.21.1 with NeoForge 21.1.250.

I’m building a shared survival world where players can focus on magic, technology, exploration or building. This repository shows the plan, the modpack snapshot and the checks behind the decisions, so others can learn from the work while it develops.

**This is a work in progress, not a finished server or a tested public pack release.** It does not include Minecraft, third-party mod binaries, private worlds or account data.

The snapshot records **139 active archives and 2 disabled archives**. Official download metadata is verified for **122 active files and 1 disabled file**. The remaining **17 active files and 1 disabled file** need manual provenance resolution. Local repair assets and most saved configuration are also excluded, so exact playable reconstruction is still blocked.

## Start here

| What you want | Read |
|---|---|
| Understand the intended player experience | [Server plan](docs/server-plan.md) · [Downloadable illustrated HTML](docs/server-plan.html) |
| See the engineering decisions and limits | [Case study](docs/engineering-case-study.md) |
| Follow the next development steps | [Roadmap and acceptance checks](docs/roadmap.md) |
| Inspect or reconstruct the development modpack | [Modpack snapshot and setup](modpack/README.md) · [Readable mod list](modpack/MODLIST.md) |
| Learn how to help | [Contributing](CONTRIBUTING.md) |

The separate [pack handbook](https://github.com/faizsaifulnizam/minecraft-pack-wiki) is for player and LLM reference. Its baseline can differ from this development snapshot; do not assume both repositories describe the same installed state.

## What is here today

- A public copy of the server brief, including original diagrams and clear open decisions.
- An exact installed-file catalogue for the separate **Upcoming-Mods** development branch, with hashes and upstream download references where verified.
- A reconstruction guide that names missing/manual prerequisites instead of silently substituting different mod files.
- Small Python checks for the catalogue and packaging boundaries.
- A roadmap that separates selected features, installed files, static checks and gameplay acceptance.

The development branch contains additions that have not passed game or multiplayer testing. Historical tests of the earlier base do not certify this combined snapshot. A successful metadata or archive check is not a performance result.

## The server direction

- A starter town introduces the world and explains the main choices.
- Magic, exploration and technology each need viable routes to shared goals, without forced personal progression through the other disciplines.
- One shared economy and coherent Tensura/Solo Leveling character rules need explicit integration.
- Players can choose world exploration or hub-accessed procedural dungeon runs.
- Collectible shared mounts, pets and small player/NPC parties are planned systems, not completed features.
- Create is excluded from this project.

The plan is intentionally more detailed than the current implementation. Read the status beside each feature before treating it as available.

## Selected starting foundations

These are **selected for future integration, not newly installed by the selection**:

| Foundation | Intended role |
|---|---|
| Lightman’s Currency + LCompat | Shared money, supported shop and claim-sale connections |
| Transmog | Equipment appearance changes |
| Dimensional Dungeons | Procedural dungeon generation |
| Silent’s Power Scale | A mob-difficulty extension point |
| Kindred | Collection, summoning and recovery building blocks |
| Waystones | Destination-to-destination travel |

Use existing configuration and supported integrations first. Custom code should fill proven gaps, not replace working systems for the sake of writing more code. Kindred’s conflicting licence declarations still need clarification before copying its implementation.

## Check the repository locally

Use Python 3.11 or newer from the repository root:

```sh
python scripts/verify_modpack.py --self-test
python scripts/verify_modpack.py
python scripts/check_public.py
```

These checks do not launch Minecraft or install mods. See the [modpack guide](modpack/README.md) for what can be reconstructed and what remains manual or blocked. Do not treat this catalogue as a ready dedicated-server distribution.

## Portfolio context

**Project owner:** Muhammad Faiz Saifulnizam.

This is an AI-assisted learning and engineering project. I set the product direction and review the choices. AI tools help with research, documentation, scripts and checks. The mod authors own their mods; I am not claiming to have written them.

The work shown here is requirements design, mod integration planning, reproducible file inventories and verification. It is not evidence of measured performance gains, completed multiplayer acceptance or independent authorship of every line. The [case study](docs/engineering-case-study.md) explains the boundaries.

## Rights and safety

Read [RIGHTS.md](RIGHTS.md) before reusing material. Public visibility is not a blanket licence for third-party mods or assets. This repository links to upstream downloads rather than redistributing their binaries.

Keep saves, account files, launcher authentication, private server addresses, logs and diagnostic recordings out of contributions. Report sensitive issues through the private route described in [SECURITY.md](SECURITY.md).
