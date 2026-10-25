# Player-ready packaging during development

**Status: proposed workflow, not an installable release.** This branch adds documentation only. It does not install mods, change the selected game instance, adopt a new mod roster, generate a native platform export or authorize publication on CurseForge or Modrinth.

## Goal

Players should install one approved pack through a supported launcher and receive the required official mods, settings, custom content and fixes together. A second manual ZIP copy, JAR replacement or patch script is not the intended installation flow.

Keep upstream originals and authored work separate internally, so their identities, rights and loading routes remain clear. That internal separation should not become two player installation steps.

Prepare the minimum source structure now, prove one genuine separate fix later, then freeze and qualify the full release when development is stable. Reuse the existing tools and source organisation rather than build a custom launcher or patch framework.

## This plan versus the existing public snapshot

The existing [catalogue](../modpack/README.md), [roadmap](roadmap.md) and server-plan documents describe an earlier development snapshot. Their loader pin and some selection decisions are historical, not the final release contract. In particular, current planning selects Create and excludes the Solo Leveling family; old public wording must not cause rejected providers to be reinstalled.

This documentation push does not refresh that catalogue or certify current installed content. Before implementation, reconcile the owner-approved selection, exclusions and accepted repair revision. Do not pick a release baseline simply because an instance or archive has the newest name. The exact release loader patch, Java runtime, component roster and first platform remain decisions to qualify.

## What belongs in GitHub

| Publish after review | Keep outside the public repository |
|---|---|
| Authored source, scripts, reviewed defaults and public documentation | Played instances, personal worlds, player/team progress, maps and waypoints |
| Exact official component identities, publisher links and hashes | Authentication files, private server details and machine-specific paths |
| Rights-cleared custom source/assets and required notices | Unresolved-rights artwork, copied payloads and private rebuilt upstream JARs |
| Sanitized technical decisions, check commands and scoped results | Raw logs, profiler captures, diagnostic/review bundles and private correspondence |

A public source repository is not a distribution licence for everything used during development. Permission to include an original mod does not automatically permit modification or redistribution of copied classes, JSON, structures, textures or binary patches.

Use focused branches and one writer for shared source/metadata. A documentation branch push does not authorize a PR, merge, platform release, game deployment or workflow/settings change. Review the branch's workflow triggers before pushing. Keep the existing historical checks and their fail-closed export boundary intact.

## Stage A: establish a usable development source

This stage needs a separate source-work approval. It includes approved-input reading, local source/ledger/checker/docs work and bounded public metadata research. It excludes game/server runs, tool installation, world reads, live-instance writes and external submissions.

### A0. Record ownership and recovery before source writes

- Name the exact output set and settle one-writer ownership.
- Retain before-bytes/hashes or absence, proposed after-bytes and durable write intent privately.
- Stage candidate changes first; compare destination preimages before applying them.
- On interruption, classify each target as unchanged, this revision's exact after-bytes or foreign drift. Restore only owned after-bytes and preserve another writer's changes.

**Done when:** the intended write set and recovery inputs exist before any dependent modification. Historical catalogues and preview archives remain unchanged.

### A1. Capture a coherent approved input

- Confirm the exact stopped source and its owning workflow's closeout. Do not borrow another task's launch permission or capture its changing instance.
- Declare approved roots/files and exclusions before reading. Do not copy an entire instance or configuration folder.
- Refuse file/ancestor links and reparse-point escapes. Copy only approved world-free inputs into a unique private revision.
- Record complete membership, hashes, sizes and expected absences for that declared set. Verify the copied bytes and recheck the source map. Stop on drift without automatic rebaselining.
- Classify official originals, original custom work, modified files, unknowns and disabled entries. Distinguish archive counts from declared provider IDs.

**Done when:** downstream work can consume verified frozen inputs instead of a changing played folder. Missing provenance and ambiguous selections remain visible.

### A1b. Demonstrate one real file early

Before broad research, select one real owner-approved, rights-cleared shareable setting. Put it through reviewed source, a minimal draft ledger, the first small offline check and fresh local reconstruction. Reject an incorrect hash/size first, then verify the intended file's exact destination and bytes.

Reuse this same checker in later work. If no real setting is approved, report that blocker rather than call a synthetic example product progress. Synthetic inputs are useful for negative tests, not a substitute for the real demonstration.

**Done when:** one genuine source change traverses the local preparation path. This is not launcher installation or proof of a separate custom fix.

### A2. Reconcile the selected work and delivery routes

Account for all approved earlier, current and future requirements, not just a recent repair batch or a fixed settings count. Reconcile these categories:

- Performance, comfort, controls and presentation defaults.
- Common/server and new-world defaults.
- Custom mods and compatibility fixes.
- Datapacks, scripts, recipes, loot and progression/integration rules.
- Models, textures, animations, UI and language assets.
- Install/update guidance and approved onboarding/help content.
- Launcher/release metadata, attribution and source obligations.
- Any additional approved runtime requirement introduced during development.

Traverse mandatory dependencies and explicit client/server requirements. Rejected providers remain rejected; a hold is not a rejection. A required player outcome remains required when its old implementation is held or excluded.

**Done when:** each known mandatory item has an eligible delivery route or a named blocker/owner decision, and outstanding discovery leads remain explicit. This does not require repairing every blocker before source preparation can finish.

### A3. Stage reviewed shareable source

Author reviewed defaults and content in the release-source tree, then stage them into approved trials. Use frozen input deltas, not a wholesale copy of played settings. Preserve personal preferences/progress and historical previews.

Keep common/client/server layers explicit. Declare intentional same-path overrides, priority, activation and optional-provider behaviour. A file copied to a folder is not necessarily loaded. New `defaultconfigs` do not automatically migrate existing world `serverconfig`.

Launcher Java/memory guidance stays separate from game-directory overrides. Do not publish personal Java paths, diagnostic agents, automatic development recordings or trial heap settings as universal requirements.

### A4. Use one small offline checker

Proposed source files, **not created by this documentation change**:

```text
distribution/
  README.md
  release-ledger.json
  verify_release.py
  official-downloads/
  custom-content/common/
  custom-content/client/
  custom-content/server/
  patches/source/
```

Prefer Python's standard library and reviewed primitives from the existing [catalogue validator](../scripts/verify_modpack.py) and [public-tree checker](../scripts/check_public.py). Do not import private historical deployment builders or remove the [existing export interlock](../scripts/check_export_ready.py). Those historical scripts are not a current pack builder.

The proposed checker should validate the explicit ledger and approved staged source without fetching, building, launching or automatically fixing anything. It must distinguish a structurally valid draft from a player-ready edition. Exit success for a draft check is not release approval.

### A5. Close out honestly

Reconstruct the reviewed local content into a fresh owned destination and compare the complete path/hash/size set. Keep local copying separate from original-file acquisition and native launcher import.

The initial source-only pass is proposed as **90 minutes inclusive of preparation, verification and reporting**, starting with the first preparatory action after approval. Prioritize A0/A1/A1b, reserve closeout time, and stop with an explicit incomplete/blocker report rather than silently extend. Full rights/roster reconciliation is not promised within that allowance.

A valid result can be **SOURCE_STRUCTURE_USABLE / RELEASE_BLOCKED**. It must not be labelled a finished player install.

## One canonical ledger

Keep one current source of truth, not separately edited platform inventories. Each record needs its purpose, exact identity, provenance, selection, relevant dependencies, client/server side, destination/layer, hashes/sizes, loading route/order, rights/notices/source obligations, platform eligibility and scoped acceptance evidence.

Keep three concepts separate:

1. **Discovery coverage:** authoritative input revisions, delivery categories and unresolved leads. A green subset does not prove the list is complete.
2. **Required outcome:** the owner-approved milestone obligation and exact concrete implementations satisfying it.
3. **Implementation disposition:** selected, optional, held, excluded or unresolved.

Define `satisfied_by` as an **ALL-of set of concrete non-requirement implementations**. Every required part must qualify. Empty or held/excluded satisfiers leave an outcome unsatisfied; requirements cannot satisfy one another in a cycle. An approved replacement changes the concrete set with its decision reference instead of adding an ambiguous alternative.

For example, where a complete repair requires server-data corrections and a separate JEI code correction, a data PASS cannot qualify the outstanding code part. Do not treat historical private-JAR success as proof that either separate route works.

Unknown identities/hashes remain unknown. Do not invent file IDs, rights grants, URLs or test evidence. Drafts can contain named pending decisions; strict readiness cannot ignore them.

## Choose the smallest permitted delivery route

| Change | Preferred route | Required proof |
|---|---|---|
| Settings/keybinds | Reviewed native overrides | Fresh uptake, side and later preference preservation |
| Recipes/tags/loot/structure data | Existing pack-wide datapack/script route | Exact IDs, activation, priority and relevant provider states |
| Models/textures/animations/language | Proven resource-pack/assets route | Copied-content rights, selection and precedence |
| Original Java content/compatibility | Normal versioned loader mod | Exact dependencies, side and genuine initialization |
| Upstream Java defect | Official correction, otherwise permitted independent companion code | Correctness with publisher-original JARs |
| Early dependency/access metadata | Upstream correction or approved licensed fork | Feasibility in the actual loader phase |
| Nested pack metadata | Upstream correction or proven pack replacement | Actual pack-selection semantics, not a loose unrelated metadata file |

Technical feasibility, legal rights, platform hosting approval and actual launcher download access are separate gates. A working local patch, open-source licence or permitted hostname alone does not satisfy all four.

## Stage B: prove one genuine separate fix

Obtain a separately bounded pilot approval. Select one mandatory rights-cleared existing data/resource correction using an already installed loading route. If none qualifies, report the exact blocker; do not substitute a toy or expand into a universal patching system.

The pilot must name original artifact identities/hashes, exact changed IDs, permitted payloads/build/download effects, tuple, route/order, disposable target, positive behaviour, adjacent unaffected control, relevant provider/persistence checks, maximum starts and inclusive time/cleanup bounds.

**Success:** publisher-original JARs remain byte-identical, separate content actually loads at the intended priority, the intended behaviour changes, the unaffected control remains correct and owned resources close normally. File presence or a historical modified-JAR PASS is insufficient.

## Stage C: qualify the actual platform release

This is later work, with separately approved installation/test/publication effects.

- Freeze the exact roster and Minecraft/loader/Java targets after the required scope is reconciled.
- **Modrinth:** use its native index and common/client/server override semantics; verify exact-file rights, accepted download routes and current content/fork/disclosure rules.
- **CurseForge:** follow the current App-export/submission policy and preserve its generated manifest; qualify hosted-file and approved third-party/fork routes instead of embedding arbitrary replacement JARs.
- Recommend the first edition from actual mandatory-file coverage. Hold a blocked edition rather than omit essentials, invent a mirror or promise universal third-party-launcher support. A second edition is not mandatory before the first works.
- Import the exact export into a fresh owned destination without developer mods/configs or hidden private files. Mandatory second ZIP copies, manual JAR replacement and patch scripts fail the intended automatic-install flow.
- For clean acquisition, approve the exact owned launcher-profile/cache boundary or supported equivalent. Never purge existing user/shared caches without separate authority. Retain required-file resolution evidence, distinguish actual downloads from legitimate reuse, and compare final identities/hashes and overrides. Reuse is not itself failure, but cannot prove an unexercised download criterion.
- Qualify startup, loading/default uptake, actual behaviour, save/reopen, dedicated-server operation, two-client join and updates that preserve preferences/progress.
- If server distribution is offered, test its delivered bytes. CurseForge uses a separately qualified server Additional File attached to the matching client release, not the client ZIP; Modrinth server-only overrides apply only in the server environment.

Bind each advertised edition/launcher claim to the exact export hash, target, source/ledger revision and current acquisition/import/runtime/server/update receipts. All-green component records cannot qualify a missing or unimported assembled export.

## Planned checks and negative controls

All checks below are **NOT_RUN for the proposed product workflow by this documentation change**.

| ID | Case | Expected result |
|---|---|---|
| T01 | Valid draft with unresolved target/rights/requirements | Structural pass; strict readiness refusal |
| T02 | Real approved shareable setting | Exact local path/hash reconstruction |
| T03 | Same-size tamper, missing file or extra staged file | Each refused for its own reason |
| T04 | Duplicate/unsafe path, traversal or link escape | Refuse before following/reading unsafe targets |
| T05 | Required dependency missing, held, excluded or side-incompatible | Refuse dependency closure |
| T06 | Original inclusion allowed but copied-patch rights unknown | Patch readiness remains blocked |
| T07 | Ineligible platform download route or mandatory manual step | Edition blocked; no bypass |
| T08 | Old repaired-JAR PASS attached to a new separate route | New route remains unqualified |
| T09 | Owned dummy forbidden subtree and dummy sensitive value at an allowed path | Membership-first and bounded authored-content refusals; never inspect real forbidden files |
| T10 | Intentional layered override versus accidental collision | Accept only declared precedence; no client-only server content |
| T11 | Real separate fix with original JAR | Positive/control behaviour and applicable persistence/provider checks |
| T12 | Update with existing user keybind/world configuration | Preserve state or use explicitly approved migration |
| T13 | Green entered rows but pending discovery category/lead | Strict readiness refuses incomplete coverage |
| T14 | Required outcome has no eligible selected satisfier | Remains unsatisfied |
| T15 | Same payload but changed target/dependency/provider/route/order | Old PASS stays historical |
| T16 | Green components but absent/wrong export or launcher-import receipt | Strict edition readiness refuses |
| T17 | Shared cache conceals unobserved required acquisition | No clean-acquisition credit without approved isolation/evidence; existing caches untouched |
| T18 | Data part PASS but required code part NOT_RUN | Complete repair remains unsatisfied |
| T19 | Requirement used as satisfier leaf or requirement-only cycle | Refuse circular/artifact-free credit |

Use owned synthetic fixtures for refusal checks, never actual personal/auth/world data. Match each negative to its intended reason so an unrelated earlier failure cannot hide an absent guard. Bounded screening is not proof that every possible secret is detectable.

## Maintain this during development

For each selected change, update its source and ledger in the same task, check affected rights/routes/versions, run affected authorized checks and record remaining gates. Bind evidence to current target/dependency/provider identities, side, payload and route/order. Keep stale PASS historical; requalify the affected boundary after changes rather than rerun an unrelated full suite for every text edit.

Prepare reviewed public commits from explicit allowlists. Keep bug/technical history truthful and sanitized. Re-read the exact remote destination after an authorized push; verify hosted checks separately from local results. Publishing source is not permission to merge, deploy a server or advertise a finished pack.

## Evidence and next approval

The private planning proposal underwent two rounds of three scoped reviews, with twelve findings addressed. The final integration received parent checks; it was not given a third independent signoff. Those planning checks are not product execution, legal clearance or runtime acceptance.

Before Stage A, review the proposed design/plan, confirm the exact stopped baseline and accepted repair revision, approve the limited read/write scope and choose the execution approach. Parent-led integration is recommended because the ledger/source/checker share interfaces; parallel research is useful only where scopes genuinely separate. Later pilot, export, live tests and publication need their own exact permissions and budgets.

Current repository checks remain useful for the historical source tree only:

```sh
python scripts/check_public.py --self-test
python scripts/check_public.py
python scripts/verify_modpack.py --self-test
python scripts/verify_modpack.py
```

These do not implement the proposed release checker, launch Minecraft, establish current dependency/rights closure or certify the eventual pack.
