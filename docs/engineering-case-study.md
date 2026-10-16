# Engineering case study: turning a modpack into a coherent server

**Status: development and learning project, not a production-ready server.** Target: Minecraft 1.21.1 and NeoForge 21.1.250. This case study records design and evidence boundaries as of 16 October 2026. See the [roadmap](roadmap.md) for acceptance milestones and the [server plan](server-plan.md) for the player-facing direction.

## The problem

A large content pack gives players many activities, but it does not automatically give them a coherent multiplayer experience. Technology, magic, character progression, settlements and dungeon exploration can each work on their own while disagreeing about rewards, ownership, death and progression.

The owner chose a fantasy/tech RPG survival multiplayer server with a starter town and onboarding. The engineering problem is to connect those systems without forcing every player through every discipline, creating competing sources of truth or risking saved progress. Adding another mod is useful only when it fills a demonstrated gap.

## Responsibility and evidence

This is pack curation, requirements work and integration planning. It is not a claim to have authored Minecraft, NeoForge or the third-party mods.

| Evidence class | What is supported | What it does not establish |
|---|---|---|
| Owner product choices | Server identity, player rules and selection of starting foundations | Implemented mechanics or passing tests |
| AI-assisted research | Candidate comparison, public-source inspection, release metadata review and draft documentation, checked against retained evidence | Author endorsement, legal permission to copy, exact binary compatibility or gameplay success |
| Recorded static installation work | Separate Upcoming-Mods instance, approved additions, archive/dependency/hash checks and saved configuration checks | Startup, effective configuration loading, world generation, balance or multiplayer acceptance |
| Owner-reported gameplay | Owner feedback says the existing combined core gameplay works within the reported scope | Independent reproduction or acceptance of each proposed feature |
| Future runtime acceptance | Explicit test scenarios and required observations | Completed tests; these gates remain open |

The owner sets the product direction and approves changes. AI assistance helps gather and organize evidence, but a recommendation is not permission to install, launch, publish or copy source. This public case study condenses the decisions rather than exporting private development logs.

## Constraints that shape the design

- Keep the existing main baseline separate from Upcoming-Mods. A development launcher instance is not a Git branch or a release guarantee.
- Use Minecraft 1.21.1 / NeoForge 21.1.250 as the target, so a project name or a broadly matching loader label is not enough for compatibility.
- Exclude Create and its addons. Use the existing industrial and storage direction rather than reopen that choice.
- Keep MCA external villager chat AI disabled. The saved configuration was checked; effective runtime behavior still needs a permitted test.
- Preserve complete magic-only, exploration-only and tech-only routes to agreed shared goals. Optional cooperation must not conceal a mandatory dependency on another specialist.
- Treat hosting capacity, responsiveness and recovery as questions to test. The selected hosting direction and tentative allocation are not deployment or capacity evidence.
- Respect separate code, asset and dependency licences. Public source visibility does not grant reuse rights.

## Design decisions and their trade-offs

### Reuse a supported integration before replacing it

The owner selected Lightman's Currency with LCompat, Transmog, Dimensional Dungeons, Silent's Power Scale and Kindred as starting foundations, with Waystones for travel. **These selected foundations are planned, not installed.** Their release labels and inspected source are research leads, not full-pack clearance.

LCompat changed the economy recommendation because research found existing Waystones-money and FTB Chunks claim-shop integration. That is a concrete reason to evaluate its supported behavior before writing a new bridge. It does not prove arbitrary plot geometry, one currency across all trades or crash-safe payment and ownership transfer. Optional rent and travel fees are not selected merely because a mod offers them.

### Separate appearance from functional equipment changes

Transmog is a candidate for appearance transfer. Functional ability transfer is a different problem: an adapter must identify the supported ability without importing donor damage, armour or unrelated state. Enhancement, enchantment and socketing also need separate rules. Treating all these as one item-copy operation would hide both balance and data-loss risks.

### Separate dungeon generation from run ownership

Dimensional Dungeons is a candidate generation backend. A generated dungeon in another dimension is not proof of an isolated party run. Admission, safe return, full-party-wipe reset and completion rewards need an explicit lifecycle. A reset must never clean up persistent-world areas or remove surviving players' run state.

### Keep each source of truth explicit

Permanent membership and claim access belong to the unified FTB Teams/Chunks direction. Temporary expedition parties must not grant home access. The installed Tensura/Solo bridge must be audited before adding another character or XP authority. Similarly, one companion recovery authority must own death and respawn state so two systems cannot revive the same entity.

Silent's Power Scale exposes a useful difficulty extension seam, but the hub-distance policy, rank labels and all-mob coverage are separate requirements. Labels, attribute effects and rewards require separate checks, including passive mobs, villagers, bosses and summons.

### Treat collection, pets and mounted travel as different contracts

Kindred is a partial collection/summoning lead, not a complete pet or mount solution. Its conflicting hosting and repository licence declarations prevent assuming source-copy permission. Evaluation must also establish global follower limits, idle anchors, damage rules and recovery. Actual multi-player mount seats and rider safety require their own evidence.

### Defer equipment rewards without moving the failure elsewhere

The planned equipment-token pipeline replaces eligible equipment drops, evaluates keep-filters at redemption, creates kept equipment and converts rejected outcomes directly into the common currency. It must preserve non-equipment loot and prevent original drops plus tokens being awarded together.

This is a design intent, not a measured optimization. Unique physical tokens can still flood the world, and a large redemption batch can move work into a new spike. Entitlement aggregation, bounded processing and separate farm/redemption measurements belong in acceptance before claiming any performance benefit.

## What has actually changed

Retained installation records describe a world-free Upcoming-Mods development instance kept separate from main. Approved work added MCA Reborn and MCA: Conversations, Terralith, structure/exploration additions and the Fresh Animations: Player Extension resource pack. Tectonic was retained. The historical Upcoming snapshot records 139 active top-level JARs; this is a dated inventory fact, not a current release count or quality measure.

Static records include archive integrity, declared dependency ranges, available publisher hashes, installed-byte readback and scoped preservation checks. Publisher digests were not available for every artifact, so local hash checks must not be described as universal publisher verification. MCA external AI was explicitly disabled in the saved configuration.

No Minecraft launch or main promotion was recorded for those Upcoming additions. Terrain placement, combined world generation, visual behavior, effective AI configuration, dedicated-server behavior and performance remain unaccepted. The newly selected foundations listed above were not installed by the research or by this documentation export.

## Evidence strategy

Use a claim ladder rather than a single “works” label:

1. **Availability:** identify the exact project, release and target listing.
2. **Static suitability:** inspect selected binary dependency/loader bounds, archive integrity, required sides and applicable terms. Source and release correspondence may remain unresolved.
3. **Isolated runtime behavior:** with separate approval, test one narrow promise in disposable state and retain expected versus observed results.
4. **Integration behavior:** exercise two clients, mixed mod interactions, permissions and save/rejoin/restart failures.
5. **Release readiness:** prove recovery, onboarding and representative workloads on the actual deployment before advertising them.

Record the pack revision, scenario, expected result, observed result and limitations for each test. Separate client frame behavior, server simulation and network response. An error-free startup does not prove gameplay correctness, and an owner report should remain labelled as such. No performance gain, supported player count or completion metric is claimed here.

## Learning outcomes and limitations

The reusable lesson is how to reduce uncertain integration work: express player promises as invariants, find existing supported seams, separate permanent identity from temporary participation and test failures as well as the happy path. Research also corrected an initial omission of LCompat, showing why a candidate comparison should remain open to primary-source corrections.

The delivered outcome so far is a clearer requirements model, a bounded static development baseline and a staged acceptance plan. It is not a completed economy, character framework, pet engine or dungeon service. Exact Tensura absorption hooks, NPC progression support, transaction recovery, mount seating and complete discipline routes remain unresolved. Readers can study the method and the [next acceptance slices](roadmap.md), but should not treat the repository as a verified server deployment.

## Public references

These are primary learning references used by the retained research, not newly revalidated compatibility certificates:

- [FTB Teams documentation](https://docs.feed-the-beast.com/mod-docs/mods/suite/Teams/) and [FTB Chunks documentation](https://docs.feed-the-beast.com/mod-docs/mods/suite/Chunks/): membership versus claim responsibilities.
- [LCompat selected release](https://www.curseforge.com/minecraft/mc-mods/lcompat/files/7942926): an existing compatibility route worth evaluating.
- [Transmog appearance component](https://github.com/Hidoni/Transmog/blob/e64233b696f0934135cf25b179f79e5d17ba7756/Common/src/main/java/com/hidoni/transmog/component/TransmogAppearanceItem.java): separate cosmetic data from the underlying equipment.
- [Silent's Power Scale extension event](https://github.com/SilentChaos512/Power-Scale/blob/842da38ea8f68769503d7660799f440f58451767/src/main/java/net/silentchaos512/powerscale/api/event/SetMobDifficultyEvent.java): a candidate integration seam, not the complete server policy.
- [Kindred repository licence](https://github.com/Silvertide7/kindred/blob/main/LICENSE.md): resolve the recorded declaration conflict before considering copied code; this moving link is not a licence clearance.

No third-party code or assets are reproduced in this case study.
