# Roadmap: small acceptance slices before a server release

**Target:** Minecraft 1.21.1 / NeoForge 21.1.250. **State:** development, not release-ready. This roadmap describes future work, not permission to install or launch anything. See the [case study](engineering-case-study.md) for evidence boundaries and the [server plan](server-plan.md) for product direction.

The owner selected Lightman's Currency + LCompat, Transmog, Dimensional Dungeons, Silent's Power Scale and Kindred as the starting foundations, plus Waystones for travel. **All are planned, not installed.** Historical Upcoming-Mods installation records cover other approved additions and static checks only; they do not close these milestones. No dates or player-capacity promises are assigned.

## Invariants: do not tune these away

- **Party capacity and XP:** at most four total members, including the controlling player and NPC companions. Per-member leveling XP is **100% / 55% / 40% / 40%** of the solo base for one/two/three/four members. This is not a fixed pool divided equally. NPC companions consume party slots, not the one-following-pet allowance. Do not redirect unsupported NPC XP to an owner. Nearby eligibility, bracket counting, rounding and supported NPC progression still need explicit rules. Loot settings must not alter these rates.
- **Pets and NPC recovery:** idle pets are invincible and return to their recorded idle anchor after a displacement delay. Each player has at most one following pet across supported sources, not necessarily one owned pet. Following pets ignore environmental damage, remain vulnerable to mob damage and respawn after a timer. NPC companions use those protection/recovery rules but party capacity instead of the pet slot. Timers, mixed damage sources, player damage and simultaneous pet-plus-party policy remain open.
- **Death and instances:** keep inventory, including supported modded slots, without duplicate drops. Deduct only progress toward the next RPG level, never earned levels or unlocked abilities. Normal death uses bed respawn; instance death uses the correct portal entrance. One death must not reset a surviving party's run. Full party wipe resets; solo death is a solo wipe. Major rewards issue once after completion. Penalty amount, safe fallbacks, wipe membership, incidental reward retention and re-entry remain open.
- **Independent disciplines:** magic-only, exploration-only and tech-only players must each have a complete route to agreed shared outcomes without personally progressing another discipline or depending on another player to remove a mandatory blocker. Signature mechanics may retain native requirements, but shared progression cannot hide cross-discipline gates.
- **Travel and permissions:** Waystones and collectible summonable, invincible ground/water/flying mounts are the main travel direction. Offered mounts need a driver and at least one actual player passenger. Independent player flight is disabled server-side, while mounted flight remains available. Mount invincibility does not imply rider immunity. Temporary parties never grant permanent claim access.
- **Integration boundaries:** one server currency; no donor-stat copying during appearance/ability transfer; unsupported mob Tensura skill associations are inert until eligible absorption grants a functional player skill. Preserve supported existing mappings. No Create or addons, and MCA external AI stays disabled.

## How a milestone closes

Every runtime milestone below is **pending and unperformed**. First obtain separate approval for its concrete installation/test scope, then use disposable state, record the exact revision and compare observed results with the exit checks. A failed or blocked check leaves the milestone open. Record a rollback/recovery route before persistent changes. Passing a small slice does not imply whole-pack acceptance.

## 1. Freeze the candidate trial contract

**Small output:** one exact-version dependency, side-placement and rights table for the selected foundations.

**Exit checks:**
- Establish binary-enforced loader/dependency bounds and required client/server placement, including reused libraries. A target listing alone is insufficient.
- Record source-to-release uncertainty and code/asset/dependency terms separately. Resolve Kindred's licence conflict before copied-code reuse; do not copy code or assets as part of discovery.
- Preserve main and keep the development instance separate. List a rollback path and unresolved checks before proposing an approved install.

## 2. Prove one economy and travel transaction

**Small output:** an approved isolated Lightman's Currency + LCompat + Waystones evaluation, not a full economy.

**Exit checks:**
- One supported earning/spending path uses the intended balance and survives rejoin/restart without duplicate or lost value.
- Two clients demonstrate authorized and denied Waystone access plus safe failure recovery. Fees remain off/unselected unless separately approved.
- Evaluate one chunk-aligned optional plot sale if its geometry is accepted. Insufficient funds, competing buyers and retries cannot double-charge or double-sell. Town roads remain protected, and open-world claiming works without a town purchase.

**Still separate:** all legacy trades, arbitrary plot geometry, rent, final prices and a server-wide economic balance pass.

## 3. Prove appearance transfer without stat transfer

**Small output:** one vanilla and one representative modded equipment appearance test with Transmog.

**Exit checks:** look changes while target numeric stats and existing upgrade data persist after reload; preview/cancel/accept results match server state. If payment is added, confirm one charge at commit and no item/currency loss on failure or retry.

**Still separate:** functional ability transfer, donor consumption, anvil entry point and enhancement/enchantment/socketing. Before functional transfer, approve a small ability allowlist and prove no donor stats or unrelated components cross the boundary.

## 4. Establish character and danger authority

**Small output:** a field/event ownership map for the existing Tensura/Solo bridge, followed by one bounded mob-scaling adapter trial.

**Exit checks:**
- Trace actual XP, stat, class/race and death ownership without adding a competing progression framework. Rejoin/restart and repeated events do not duplicate grants or modifiers.
- Define hub origin and readable danger bands, then verify assignments separately from displayed ranks and attribute effects. Player Waystones do not become new low-danger origins.
- Reconcile an entity-ID inventory including passive/neutral mobs, villagers, bosses and summons. Test representative spawn/reload/transformation cases and transported-mob town safety. Document missing coverage rather than call it universal.

**Still separate:** complete all-mob coverage and balance. Silent's Power Scale is a candidate seam, not proof of either.

## 5. Prove party accounting before complex expeditions

**Small output:** a controlled XP event with supported player and mixed player/NPC rosters.

**Exit checks:** all four fixed per-member rates match the base reward, each recipient is credited once and a fifth member is rejected, including concurrent invite/respawn cases. Freeze recipients per event, exercise the selected range/dead/offline and rounding rules, and verify companion shares do not multiply owner XP. Party changes do not change FTB claim access. Show the active loot policy separately before combat.

**Decision gate:** unsupported NPC progression remains a blocker, not permission to invent an XP sink or redirect shares.

## 6. Prove one pet lifecycle, then mounted travel

**Small output:** one supported pet type under one recovery authority, then one offered mount for each travel category.

**Exit checks:** idle invincibility and return preserve the original anchor; the global one-follower limit holds; environmental immunity and mob vulnerability differ correctly; death/cooldown/restart creates exactly one recovered pet with intended ownership/data. Blocked/unloaded anchors and switching during cooldown have safe outcomes.

For each offered ground/water/flying mount, two actual players ride together. Summon/dismiss, boarding rights, dismount, hazards, logout and approved dimension/Waystone transitions cannot duplicate the mount or strand passengers. Audit independent-flight grants, including existing items and alternate unlocks, while preserving mounted flight and rider damage rules.

**Still separate:** expanded entity support and load testing. Kindred alone does not satisfy these contracts.

## 7. Prove a minimal dungeon lifecycle

**Small output:** one solo run, then one party run using the candidate generation backend.

**Exit checks:** admission and isolation work; normal death uses a bed and instance death a safe portal entrance; inventory and earned levels/abilities persist; configured next-level XP progress is deducted once. One member dying does not reset survivors. Full wipe resets safely, and major rewards issue once only after completion.

Exercise concurrent deaths, missing portals, disconnect/restart, re-entry and cleanup. Establish NPC/offline/respawning membership rules before interpreting a wipe. No reset touches the persistent world or another run. Only after this slice passes should concurrency limits and additional rewards expand.

## 8. Prove one deferred equipment reward

**Small output:** one supported equipment drop replaced by a recoverable entitlement, with a keep and reject path.

**Exit checks:** original equipment and entitlement never both award; non-equipment loot stays intact; kept equipment matches candidate data; rejection credits universal currency without delivering/dropping rejected equipment. Full inventory, repeated confirmation, concurrent redemption and restart neither lose nor duplicate an outcome.

Then define aggregation and bounded batches. Measure direct-drop farming and redemption separately before making any lag or capacity claim. Snapshot party reward ownership independently of the XP schedule.

## 9. Close skill and discipline coverage gaps

**Small output:** one existing supported Tensura mapping preserved, one unsupported entity association proven, and a shared-goal route matrix.

**Exit checks:** use verified exact-version registration/absorption/persistence hooks, not guessed APIs. The mob does not activate the associated skill; an eligible absorbing player gains the intended functional skill once. Cover restrictions, summons/respawns and save/rejoin before extending the catalogue across the entity inventory.

For each agreed shared goal, demonstrate early-to-late magic-only, exploration-only and tech-only routes with earnings/resources and no mandatory personal cross-discipline blocker. Record signature-content exceptions explicitly. A first-result tutorial is not complete progression acceptance.

## 10. Validate onboarding and deployment

**Small output:** an unfamiliar player's starter-town journey, then a dedicated-server acceptance record for one frozen revision.

**Exit checks:** the player finds help, understands danger, party loot/XP, pets, travel and death rules, chooses a route and reaches a useful first result without continuous developer guidance. Optional plots remain optional.

Audit client/server placement, effective MCA AI-disable configuration and the selected world-generation combination in a new disposable world. Prove two-client join/rejoin, representative base/combat/exploration and dungeon workloads, backup export and restore on the intended hosting setup. Record client behavior, server responsiveness and network response separately, then choose evidence-based budgets. The tentative hosting allocation is not a capacity guarantee.

**Release gate:** promote only with explicit owner approval after the advertised promises pass, unresolved exceptions are visible and rollback/recovery is demonstrated. A public learning repository is not permission to open a public game server.
