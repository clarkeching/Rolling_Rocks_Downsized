# Rolling Rocks Downsized — Condensed Rewrite

## About Clarke
- Not a developer. Explain things in plain language.
- Prefers action over questions. Just do the thing, don't ask permission for every step.
- If something breaks, fix it. Don't present options — pick the best one and do it.

## Project
Condensing the 73k-word business novel "Rolling Rocks Downhill" into ~20-25k words. Commercial product Clarke will sell. Title: "Rolling Rocks Downsized."

## Session Startup
At the start of every session, BEFORE doing anything else:
1. Read `Session Log.md` — this is the source of truth for what was done, what's open, and what to do next.
2. Tell Clarke what you know — briefly summarise where things stand so he can confirm or redirect.

## Key Files
- `Rolling Rocks Downhill Complete.md` — the full original book (NEVER modify)
- `Rolling Rocks Downhill - Condensed!.md` — the main manuscript
- `Part Two - Working Draft.md` — working draft for Part Two edits
- `Session Log.md` — session-by-session log of all decisions, changes, commits
- `Editorial Feedback - Rolling Rocks Downsized.md` — editorial notes and expansion priorities
- `Part Two Editorial Brief.md` — Part Two specific editorial recommendations
- `Steve's Lightbulb Moments.md` — extracted appendix content
- `Full Text/` — individual original chapters
- `Characters/` — character profiles
- `Concepts/` — key concepts

## Rules
- Always commit and push directly to the main branch. NEVER create separate branches.
- Always update `Session Log.md` after every decision, change, or commit. Include timestamps (e.g. `### Thing I did (~14:30)`).
- Always commit and push after making changes. Use descriptive commit messages.
- Never modify `Rolling Rocks Downhill Complete.md`.
- Don't ask Clarke to run scripts — run them yourself.

## Key Decisions (already made)
- **Voice**: Third person (original is first person)
- **Vibe**: "The movie version" — a 2-hour experience, not a 7-hour read
- **Keep**: Humour, silly names, character moments, four pivots, Steve's emotional arc
- **Don't teach**: Evaporating Cloud — replaced with 2x2 grid (speed vs quality) and "Darth" (the conflict cloud)
- **Cross-promote**: "The Bottleneck Rules" and "CorkScrew Solutions"
- The `> [!abstract] Chapter Summary` callout boxes are Clarke's navigation aids. Leave them alone.

## Location
- **GitHub:** `github.com/clarkeching/Rolling_Rocks_Downsized`
- **Local:** `~/Documents/Obsidian/Rolling Rocks Downsized`

## Review Workflow (Track Changes for Prose)

Clarke reviews changes on his iPad/iPhone, not at a desk. He needs to see what changed and where - like track changes, but in plain markdown using Obsidian comments.

### When you edit existing prose

Wrap the original text in `%% OLD:` and `%%` markers. Put your new version immediately after. This lets Clarke search for `%%` to find every change.

```
%% OLD:
Sarah walked into the room and sat down on the chair. She looked around nervously.
%%
Sarah hesitated in the doorway, scanning the room before choosing the seat nearest the exit.
```

### Don't comment-wrap these

- Typo fixes, spelling, punctuation
- Formatting changes (headings, spacing, callout boxes)
- New text that isn't replacing something existing
- Changes Clarke has already asked for with specific wording (just do them)

### Clarke's feedback comments

Clarke leaves comments for you inline using `%% Clarke: ... %%`. When you find these:
- Read them carefully - they're instructions or feedback
- Act on them
- Remove them once you've addressed them

```
%% Clarke: This section feels too rushed. Slow it down, add some sensory detail. %%
```

### Accepting changes

- "accept all" — strip every `%% OLD: ... %%` block from all files, keeping only the new text below each one
- "accept changes in [filename]" — do it for that file only
- Never remove `%% Clarke: %%` comments unless you've addressed them
- After accepting, commit and push as usual

## NotePlan
Daily notes: `~/Library/Containers/co.noteplan.NotePlan3/Data/Library/Application Support/co.noteplan.NotePlan3/Calendar/YYYYMMDD.md`
