## Using Claude to Condense a 73,000-Word Novel Into a Novella (In Under 10 Hours)

Twenty years ago, I wrote a business novel called *Rolling Rocks Downhill*. It's done well—still sells, still gets recommended. But at 73,000 words, it's a commitment. I've often wondered if I could create a shorter version that captured the essence without the sprawl. The kind of thing someone could read in an evening and still walk away with the core ideas.

I never had the time or energy to attempt it. Until two days ago.

I've now spent less than 10 hours working with Claude (Opus 4.5, via Claude Desktop's new Cowork mode) to produce a complete condensed edition. It's around 14,000 words. It stands alone as a story. And honestly? The quality is better than I expected I could achieve on my own, even with unlimited time.

Here's how the workflow has evolved.

### The Setup: Obsidian + Claude Cowork

I keep all my writing in Obsidian. The original novel was already there as markdown files—one per chapter, plus character notes, plot summaries, and various bits of reference material.

Claude Cowork runs in a lightweight Linux VM on your Mac (it told me this when I asked) and can access a folder you select. I pointed it at my Obsidian vault. That's it. No copying and pasting, no uploading files to a web interface. Claude can read and write directly to my vault.

(Side note: Obsidian itself seems to have got nicer recently. Maybe it's just me, but the experience feels smoother. Or maybe I'm just enjoying using it more because Claude makes the whole writing process less of a slog.)

### The Process: Conversation, Not Commands

The work has been genuinely collaborative. I'd explain what I wanted—"condense Act 1, keep the voice, preserve these specific moments that readers love"—and Claude would produce a draft. Then we'd refine it together.

Some examples of what that looked like:

- **Structural decisions**: The original book has 61 chapters. We condensed it into five parts. Claude helped me identify what was essential versus what was scaffolding I'd needed to write the full version but didn't need in the condensed one.

- **Preserving voice**: I have certain phrases readers mention to me years later. "Nibbled to death by ducklings." The rabbit/cow/hat metaphor. Claude understood which bits mattered and kept them intact while trimming around them.

- **Gap analysis**: After drafting each section, I'd ask Claude to check for "dangling references"—characters or concepts mentioned without proper introduction. It caught several and fixed them. Claude makes these sorts of mistakes while writing, just like I would. The difference is it can also systematically find and fix them.

- **External review**: I fed the draft to ChatGPT, Gemini, and a separate Claude instance to get fresh perspectives. Then Claude helped me work through their feedback systematically—adding timeline breadcrumbs, a mid-book scene to keep a character visible, clarifying a plot twist the reviewers had missed.

### Version Control: Local Git

Here's a Mac Power Users detail: Claude set up a local git repo inside my Obsidian vault. It told me what it was doing—just a few terminal commands in its Linux environment—and now I have proper version history with commit messages like "Extended small batches scene" and "Added Hal mid-book check-in."

The git repo lives in the vault folder, which syncs via iCloud. Belt and suspenders. No GitHub account required—it's entirely local unless I decide to push it somewhere later.

### What Surprised Me

The quality. I expected Claude to be useful for grunt work—finding inconsistencies, suggesting cuts. I didn't expect it to *understand the story* well enough to suggest that a character who disappears mid-book should have a callback at the end. (A text message from Steve to Craig—it works perfectly and I wouldn't have thought of it.)

The speed. Ten hours across two days, including all the back-and-forth, the external reviews, the refinements. I've spent longer than that agonising over single chapters in the past.

The collaboration. It genuinely feels like working with a skilled editor who has infinite patience, has read my book carefully, and is available at 11pm when I have an idea.

### The Result

I now have a 14,000-word condensed edition that:

- Stands alone as a complete story
- Preserves the voice and humour of the original
- Teaches the same core ideas without lecturing
- Ends on exactly the right emotional note

Is it ready to publish? Not quite—I still need to read it fresh with my own eyes. But it's close. Closer than I thought I'd get in two days.

If you've got a long-form writing project you've been putting off because it felt too big, this workflow might be worth trying. Obsidian for organisation, Claude Cowork for the heavy lifting, git for peace of mind.

I'm genuinely impressed. And I don't impress easily when it comes to writing tools.
