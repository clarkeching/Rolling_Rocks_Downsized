# Session Log

## 2026-03-02 ~09:00

### Picked up from overnight disconnect
- Recovered context from git history and memory files
- Last session (March 1) had done: Chapter 1 rewrite, editorial feedback doc, Quality and Speed chapter, Lightbulb Moments extraction, many Part One expansions
- All changes were uncommitted — committed them as "Part One rework" and pushed

### Cloud + Darth discussion
- Clarke decided the conflict cloud belongs in the story — it frames the PROBLEM (the specific dilemma), while the 2x2 grid frames the SOLUTION (you don't have to choose)
- Cloud = diagnosis, 2x2 = direction, cafeteria = evidence
- Decided to split old "Quality and Speed" into THREE chapters:
  1. **Darth** — Craig asks basic questions, draws the cloud on a napkin. Steve names the dilemma "Darth." Feels understood but more trapped.
  2. **Quality and Speed** — Craig draws the 2x2 grid. Car factory analogy. "What if there's a corkscrew?" Steve skeptical but intrigued.
  3. **You Look Like a Dork** — Cafeteria with Cheryl. Steve is discombobulated by Craig's diagnosis, not distracted by emails. Leaves because he wants practical answers, not more theory. No more fake family emergency.

### Key creative decisions
- **Craig asks "obvious" questions** — Steve answers impatiently ("obviously," "naturally") but is gobsmacked when the answers assembled together show a trap
- **Catherine callback** — Steve (not Craig) remembers Catherine's "circumstances — the ultimate bad guy" line. Realizes it's not circumstances, it's *this picture*
- **Corkscrew language** replaces "assumption" (too Goldratt). Steve's industry is trapped inside a bottle. Need corkscrew thinking — twists, not straight-line pushing. References Clarke's book CorkScrew Solutions (footnote to add later)
- **2x2 grid labels** simplified to "Good product" and "On time"
- **"What if Darth was based on a false assumption?"** changed to **"What if there's a corkscrew that pops Darth wide open?"**

### Cafeteria scene rework
- Steve's mind is on the napkins, not his emails
- He realizes his whole industry has been a car factory with rubber mallets
- Leaves because Craig's help made things worse — theoretical, not practical
- Craig's parting shot: "Cheryl was about to give you exactly the practical answers you just asked for"
- Ends with: "Darth was real. And Steve had no idea how to fight him."

### Updates to Part Two
- Grid callback at line ~1106 updated: "Remember Darth?" + grid labels matched
- Steve now remembers the cloud too when he sees the grid again

### Commits (~09:30)
1. `9b70b3a` — All working files (Ch1 rewrite, editorial feedback, Craig draft, lightbulb moments, etc.)
2. `bc6e0a7` — Main draft updated with three new Craig chapters + Part Two callback fixed

### Still open (from morning session)
- Mermaid diagram for the cloud is placeholder — Clarke will have a proper image for publication
- CorkScrew Solutions footnote to add later
- Editorial feedback's 8 expansion priorities still to work through (Egyptian Revelation scene is #1)
- "Darth" could become a recurring callback throughout the book — not yet added

---

### Part 2a bone audit (~10:00)
- Compared condensed Part Two (chapters Fowl Mood → It Worked) against original chapters 22-34
- **Verdict: bones are strong.** Logic chain complete. Nothing critical missing. Nothing unnecessary.
- Three things thinner than original but fine to leave thin:
  1. Vicious circle of hoarding (nice but not load-bearing)
  2. "In-process inspection isn't enough" bridge (covered by "but that was only the first step")
  3. Steve's homework cloud diagrams (correctly cut — Darth does the same job)

### Part 2a flavour/character audit (~10:15)
- Compared all original chapters 22-34 for joy, humour, character, visual texture
- Condensed version already surprisingly rich — most key flavour moments survived condensing
- Gaps identified in three areas:
  1. **Craig relationship** — functional but not warm enough
  2. **"Requirements Are Really Forecasts"** — emotionally flat after "face felt hot"
  3. **Steve's private vulnerability** — desperation visible but inner fidgeting missing
- Created `Part Two Editorial Brief.md` with prioritized recommendations (Tier 1/2/3)

### Part 2a rework — editorial changes applied (~10:30)
- Created `Part Two - Working Draft.md` with all changes applied
- **Two structural fixes:**
  1. Requirements chapter: added resistance throughout (air quotes, fighting his voice, banging fist, sulking, "playing word games," "an estimate/same thing," "rightish" via defiant smile, jaw drop + "Few do")
  2. Kitchen Sink chapter: expanded from 22 to ~35 lines — Star Trek fridge, worn-out mute button, scrubbing brush, radio, "Craig had rewired his eyes"
- **Tier 1 additions (all 7):**
  1. Craig's wedding detail + mother-in-law murder joke
  2. Catherine's evening quip ("good-looking single woman")
  3. "Ick" after porridge pot
  4. Grandmother's cabbage (Steve-Cheryl connection)
  5. Steve fighting his voice (Requirements chapter)
  6. Phil's fired rumour + "Not yet"
  7. "Making this up as we went along"
- **Tier 2 additions (all 8):**
  8. Craig's air quotes on "required"
  9. "An estimate" / "Same thing"
  10. Phil as "my plant"
  11. Star Trek fridge (Kitchen Sink)
  12. Cheryl slaps Steve's arm
  13. Steve sulking
  14. "Little problems" / "desperate is accurate"
  15. "I nodded in what I hoped was a thoughtful manner"
- **Tier 3 additions (4 of 5):**
  16. "Congratulations. We should get started then."
  17. Printer email from Hal's PA
  18. Worn-out mute button
  19. *Thunk* of FPP folder + Craig "Excellent!" boom
  - (Camilla the phone not added — needs more thought on how Fran fits Part Two)
- **Other fixes:**
  - Craig "more distracted than surprised" (character detail)
  - Steve "had no intention of sticking to ten minutes" (cunning)
  - Gregor "looked miserable" (emotional detail)
  - Steve "feigned surprise" (strategic reveal)
  - Physical transition into Dog Food chapter (folder thunk, Craig leading)
  - Cheryl's laugh at grandmother's cabbage (warmth)

### Commits (~10:40)
3. `4c16701` — Session Log + Part Two Editorial Brief
4. `102a519` — Part Two Working Draft with all editorial changes

### Parts 1-3 Combined file (~11:00)
- Created `Parts 1-3 Combined.md` for fresh-eyes review in another chat
- Contains Part One (from main manuscript) + Part Two + Part Three/Midpoint (from working draft)

### Fresh-eyes feedback — from another Claude session (~12:00)
- **Positives:** Opening strong, Steve feels real, pacing through Part One genuinely good, Craig's napkin scene best teaching moment, inverted pyramid reveal lands, reads like a real novel not a business book
- **Issues identified:**
  1. French Fry Revelation over-explained (told three times) — **FIXED**: cut Steve's restatement and "may contain nuts" joke
  2. "May contain nuts" joke undercuts the scene — **FIXED**: cut
  3. Catherine needs earlier moment showing commercial instincts — **FIXED**: added 6-line beat after Sticky-Note Triage where she shows she already knows which features sell the product
  4. Requirements chapter still feels Socratic despite resistance we added — noted, may need further work
  5. Phil as a plant feels convenient — kept (acknowledged in text, and it works because Steve is desperate)
  6. Team conclusions too neat — noted but acceptable for condensed version
- **Pushed back on:** Steve walking out on Cheryl (setup, not stall), Phil as plant, team neatness
- Changes applied to: working draft, main manuscript, AND combined file

### Additional edits — not logged by previous session (~12:30)
These changes were found in the working tree but not recorded in the Session Log:
1. **Norbert's threat via Craig** — new beat at start of Dog Food chapter: Craig delivers Norbert's message ("If you walk out on me this time, call him. He said he'll fly here and take over your job himself"). Steve flinches.
2. **Steve's Norbert callback** — "He tried to help. Drew some diagrams, took me to the cafeteria to show me something. But I walked out. I wanted practical answers, not napkins." (replaces vague old line, ties to walking-out setup)
3. **Cheryl's soup speech tightened** — compressed from ~12 lines of back-and-forth to 4 punchy lines. Cuts repeated explanation.
4. **"Reverse Psychology, Steve"** — new Craig line after "Why not?" in the cafeteria
5. **Cheryl second meeting reworked** — "Craig took Steve back into the cafeteria kitchen to meet Cheryl, for the second time." + Craig says "I need help" instead of Steve apologising (stronger, less repetitive)
6. **"Better food brought us more customers"** — bridge line added to connect Dog Food to French Fry Revelation
7. **Craig phone callback** — split "Craig told Steve to hold" into a hang-up and call-back (more natural)
8. **"ended abruptly"** — minor wording fix in Steve's apology to Craig

### Commits
5. `56c930c` (2026-03-03 ~10:54) — Fresh-eyes fixes + Part Two tightening + Session Log catch-up

---

## 2026-03-03 ~10:30

### Session maintenance
- Found 8 uncommitted edits from previous session (logged above)
- Committed and pushed all changes
- Updated CLAUDE.md with Session Startup rules (read memory + Session Log before doing anything, tell Clarke where things stand)
- Added rule: always update Session Log after every decision, change, or commit
- Added timestamps to all Session Log entries
- Set up `cc` alias to auto-restart remote-control sessions (no more walking to Mac Studio)

### Still open
- Mermaid diagram for the cloud is placeholder — Clarke will have a proper image for publication
- CorkScrew Solutions footnote to add later
- Editorial feedback's 8 expansion priorities still to work through (Egyptian Revelation scene is #1)
- "Darth" could become a recurring callback throughout the book — not yet added
- Requirements chapter still feels Socratic despite resistance added — may need further work

---

## 2026-03-04

### Vault moved from iCloud to Documents folder (2026-03-04 ~08:20)
- Obsidian vault moved from `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Rolling_Rocks_Rewrite` to `~/Documents/Obsidian/Rolling Rocks Downsized`
- Now syncing via Obsidian Sync instead of iCloud
- GitHub repo renamed from `Rolling_Rocks_Rewrite` to `Rolling_Rocks_Downsized`

### Git reconnected (2026-03-04 ~08:31)
- `.git` directory didn't survive the move — reinitialised git in new location
- Connected to GitHub via HTTPS (SSH keys not configured, HTTPS works)
- Restored full commit history from remote with `git reset origin/main`
- Restored `.gitignore` that was lost in the move
- Committed and pushed current state

### Aliases and config updated (2026-03-04 ~08:43)
- Updated `rr` alias in `~/.zshrc` to point to new vault location
- Updated remote URL from `Rolling_Rocks_Rewrite` to `Rolling_Rocks_Downsized`
- Updated local path in `CLAUDE.md`

### Commits
1. `794d0cc` — Reconnect git after vault move from iCloud to Documents folder
2. `7f8fd2d` — Update local path in CLAUDE.md to match new vault location

### Still open (as of 2026-03-04)
- Mermaid diagram for the cloud is placeholder — Clarke will have a proper image for publication
- CorkScrew Solutions footnote to add later
- Editorial feedback's 8 expansion priorities still to work through (Egyptian Revelation scene is #1)
- "Darth" could become a recurring callback throughout the book — not yet added
- Requirements chapter still feels Socratic despite resistance added — may need further work

---

## 2026-03-03 ~14:00

### Dog Food section moved from Part 2 to Part 1 (~14:00)

**Decision**: Clarke decided the Dog Food section with Cheryl should move from Part 2 back into Part 1. Steve actually hears the story during his first visit, but leaves on good terms — not sulking, not making excuses, just genuinely unconvinced that a cafeteria turnaround applies to software.

**What changed in Part 1** ("You Look Like a Dork"):
- Completely rewritten from ~48 lines to ~130 lines
- Drew heavily from original novel (Chapters 16-17-18)
- **Added from original**: Randall the server, Cheryl on phone with clipboard, Craig explaining outsourcing context while they wait, the hug, "computer whiz kids from upstairs," kitchen tour with sensory detail (walk-in chiller, onions frying), "I've seen you in the queue," bain-marie serving area, "she called him a newbie," full Dog Food story (big opinionated lady from Dundee, one horrifying condition, soup nobody tasted, idiot-proof rules, late inspection → in-process inspection), "French Fry Revelation" teaser, Cheryl walking off without goodbye, Craig-Steve private conversation
- **Steve's departure**: Polite, warm, genuine. Thanks Cheryl sincerely. Shakes Craig's hand. Puts tie back on. Leaves thinking "Nice story. Wrong industry." Not angry, not defensive — just a man who can see a kitchen turnaround but can't see how it scales to 47 million lines of code
- **Closing beat preserved**: "Darth was real. And Steve had no idea how to fight him."

**What this sets up for Part 2**:
- Steve already knows the Dog Food story — Part 2 doesn't need to retell it
- Cheryl liked Steve (he was respectful) but was frustrated he didn't stay for the full story
- Craig offered help, Steve politely declined
- When Steve comes back desperate in Part 2, the emotional weight is: "I should have listened. I was wrong."

### Part 2 suggestions (not yet applied — Clarke to approve)

#### 1. "The Story So Far" box
**Current**: "the one person who might have been able to help—Craig Lally, the quality guy from upstairs—Steve walked out on."
**Fix**: Steve didn't walk out. Something like: "Craig Lally offered to help him work differently. Steve thanked him and left."

#### 2. Norbert conversation ("Start Looking for a New Job")
**Current**: "He tried to help. Drew some diagrams, took me to the cafeteria to show me something. But I walked out."
**Fix** (from original Ch 22): Steve: "He couldn't help me with FPP. That was my priority. He wanted to help me prevent my next FPP." Norbert: "He said your conversation was brief, that you seemed reluctant to engage further but that you parted on good terms."

#### 3. "Ten Minutes" chapter
**Minor fix**: "apologized for how their earlier meeting had ended abruptly" → "apologized for not calling back sooner"
**Enrich with original novel detail** (from Ch 23-24):
- Craig "more distracted than surprised"
- "Little problems" / "desperate is accurate" exchange
- Craig's son's wedding this weekend, family in from around the world, three-week vacation
- "Your timing, from your point of view, sucks."
- "Congratulations. We should get started then."
- Norbert's threat via Craig: "He said if you walked out on me this time, call him. He said he'll fly here and take over your job."
- FPP folder *thunk* on the table
- Craig's "Excellent!" boom

#### 4. "The Dog Food Problem" chapter — MAJOR REWORK
**Problem**: Steve already heard the full story in Part 1. Currently retells it from scratch.
**Suggested approach**: Merge into "The French Fry Revelation." The new combined chapter:
- Cheryl: "You again?" (but warmer — she liked him last time)
- Steve: "I should have stayed for the French Fries."
- She studies him. Something is different. Less polished, more worn.
- Brief callback: "Last time, you heard about our Dog Food Problem. Remember?"
- Steve nods.
- "Good. That was the first step. Now let me show you the second."
- Straight into French Fry Revelation

#### 5. French Fry Revelation — ENRICH (closer to original novel)
Add from original Chapters 25-26:
- Bain-maries and heating lamps (physical texture)
- "Have you tasted two-hour-old cabbage?" / grandmother callback
- Big-batch timing: cooked at 10:30, horrid by 2pm
- Oil in curry trick (comedy + teaching)
- Overproduction/underproduction (Craig's formal terms — important concept)
- "Some days we'd do both" — too much soup, not enough lasagna
- Small-batch soup detail: cook smaller, switch flavors if unpopular
- High Street espionage: visiting good lunch shops, buying Subway-style ovens
- "Not bad, eh?" / Craig: "Not bad at all."
- Thinning the menu (maps to descoping in software)
- Cheryl slaps Steve's arm when he gets something right
- Steve's honest internal: "It all made perfect sense. To them."

#### 6. General principle: novella, not summary
Throughout Part 2, show scenes rather than summarize them. Add from original:
- Steve's head in hands after Norbert's call
- Powering down phone after Eleanor's voicemail
- Cafeteria emptying as evening approaches
- Evening shift workers in casual clothes

### Still open
- All Part 2 suggestions above — awaiting Clarke's approval before applying
- Mermaid diagram for the cloud is placeholder
- CorkScrew Solutions footnote to add later
- Editorial feedback's 8 expansion priorities still to work through
- "Darth" callbacks throughout the book — not yet added
- Requirements chapter still feels Socratic
