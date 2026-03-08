# Chapter 51 - Full Text

**Current Date:** Monday, October 16th *(continued)*

---

[[Chapter 51 Full|← Back to Chapter 51 Summary]]

---

Chapter 51
==========

I stood outside Ron\'s office at the opposite corner of the building. It
was 8:36 p.m.

I took a deep breath, knocked, then pushed the door open.

Ron sat there at his desk, typing in the dark, his face lit up in dull
green by the reflection from his screen. Green meant he was looking at
old mainframe code. Without bothering to look up, he mumbled, \"Just a
moment,\" and kept on typing. As I waited, I looked at his desk, which
was stacked high with books and papers. Wyx-Fin Group\'s clear-desk
policy was one of many rules that didn\'t apply to Ron.

When he finally looked up, he had a smile on his face, but that dropped
away when he saw it was me.

\"Steven.\"

\"Nice to see you too, Ron.\"

\"You\'ve come about the FPP review.\"

\"Review?\"

\"Oh \... didn\'t Eleanor tell you?\" He smiled, and I thought, looked
pleased with himself.

I shook my head.

\"While you were away, she and Norbert asked me to run an independent
assessment of FPP\'s health.\"

I shrugged. Who could blame them?

\"Give me a minute.\" He clicked a few times and his printer (no one
else in the entire building, except Hal\'s PA, had their own printer)
whirred behind him. Its lights flashed as it warmed up and I felt my
shoulders tense.

\"How about you give me the two-minute version?\"

\"I\'ll give you the three-word version instead: they\'re fine.\"

Unfortunately, in Scotland the word *fine* can mean anything from
*Excellent* to *Okay* to *I\'ll tell you it\'s fine, but only because
I\'m too polite to tell you it\'s not*. But since Ron was grumpy,
opinionated and not the sort to hold back, I nodded and said, \"Great.
Thanks.\"

Then I added, \"That\'s two words, not three.\"

\"Technically, \'they\'re\' is two words, Steve.\"

\"Okay.\" I didn\'t know if he was right, but he usually was. And when
he wasn\'t ... Honestly, it wasn\'t worth the effort arguing.

The printer ejected a single page and stopped. Ron passed it to me. For
Eleanor Scharlau and Norbert Billings was written at the top.

\"Read it. I think you\'ll be pleasantly surprised.\"

Ron and I didn\'t always get along so well, but I valued his opinion far
more than I thought he valued mine. He wasn\'t a bad old guy, just worn
down by the years, I guess.

I jumped directly to the last paragraph, which is where the gotchas
normally hide.

I, the author, have only one concern: In order for incremental
development to work, each increment must be good enough to ship. I have
seen no proof, as of yet, that this is indeed the case on FPP. Who knows
what trolls lie under the bridge until we look under said bridge?

I said, \"Trolls?\"

He scowled. \"Read the whole thing first.\"

My jaw dropped when I read the first paragraph:

FPP\'s approach to delivering software (the so-called \"inverted
pyramid\" approach), is merely a variation on well-established
incremental delivery methods, which have been used by considerably
larger software development projects for decades.

\"Incremental delivery methods\"?

He nodded.

\"What do you mean by the word incremental?\"

\"At the start of a project, you prioritize your features, then deliver
them in chunks of code which are fully tested and---to use your
term---good enough to ship. Each chunk is an increment, though some
people also refer to an increment as the period of time taken to build
the increment. Sound familiar?\"

I nodded reluctantly. \"But ... that means my inverted pyramid
approach \... it already exists?\"

\"That should be clear, given my choice of words.\"

\"I thought, well ... I thought I\'d, like ... I\'d invented it.\"

He laughed, but I couldn\'t tell if he meant it in a friendly kind of
way or if he was mocking me. \"You inverted the pyramid, but you didn\'t
invent it. You rediscovered it. And renamed it. It\'s just a shame you
didn\'t think to do it at the start of FPP, rather than after you\'d
built all that code, but otherwise, you did well.\"

I crossed my arms. \"Are you sure about this?\"

He didn\'t react initially, but then he smiled in a way that made me
uneasy. He said, \"You want proof, lift my monitor.\"

I scrunched my face up in a \"huh?\" expression.

He gestured toward his desk. I looked there for a large lizard. It must
have been hiding, because I couldn\'t see it.

\"Come on. Lift it.\" He pointed at his computer screen. \"I need one of
the books boosting it.\"

I lifted the monitor and he pulled a thick, blue book from the top of
the pile.

I put the monitor back in its place as Ron wiped the layer of dust from
the book\'s cover.

I read the title out loud. *Software Engineering Economics*. It was by
Barry Boehm. I knew of the book and the author. Both had been
influential in the 70s and 80s, the early years of commercial software
development.

\"That\'s the book with the original cost of change curve, right?\"

He raised his eyebrows. \"I\'m surprised you knew that.\"

He opened the book and thumbed through the pages until he found the one
he was looking for.

\"Page forty-one,\" he said. He stabbed the page on the heading 4.4
Refinements of the Waterfall Development, then pulled his finger down
the page until it rested below a sub-heading near the bottom.
Incremental Development.

He turned the book to face me and I read the first paragraph*:
Incremental development should develop software in increments of
functional capability.*

Ron flipped to the next page and we continued reading side by side.

Boehm described incremental development as a refinement of the waterfall
mode, whereby much of the planning, analysis and design was done up
front, but the functionality was built and tested in increments. One of
its advantages, he wrote, was that functional increments were much more
helpful and easier to test than intermediate-level components. Another
advantage is that they provided a cheaper way to include user experience
feedback into the product, earlier.

Incremental Development had been successfully used on what Boehm
described as extremely large projects (one which cost over a hundred
million dollars, way back in the 70s) as well as small projects. I found
that last bit about smaller projects particularly interesting. I could
easily see how an eighteen-month project could be chopped up into three
six-month increments or six three-month increments. I could also easily
imagine delivering a six-month project as three two-month increments. In
those cases, an increment was just a smaller project---a smaller batch.
I found it harder, though, to imagine how a two-month project could be
broken down into four or eight smaller chunks.

Thankfully, Boehm gave a simple example of a small incremental project
for a software estimation package. The first increment delivered basic
functionality: bulk input, some calculations, simple printout. The
second built upon the first increment, adding the ability to save and
retrieve previous runs and to modify data. The third increment added
optional but useful features, like schedule calculations and activity
breakdowns.

I pointed at the book, \"This is interesting, but right now I\'m
worried. I need your help. How do I know if our software is truly
GETS?\"

\"When did Boehm know his estimation software was truly GETS?\"

There really was only one answer. \"After they launched their first
increment?\"

He nodded, and after ten minutes of work around his whiteboard we had a
solution. We would ship FPP into our live environments immediately. If
things went smoothly, then good; if not, then even better; we\'d found
problems and we could fix them while we still had runway ahead of us.

Once we\'d shipped we would be live, from an engineering perspective,
and Catherine\'s team could set up their first few live test accounts to
kick the tires, but they wouldn\'t do much more than that. And, since we
were live, we would have to switch into S and M mode, using Ron\'s
teams\' processes to make small, incremental updates to our production
software.

It sounded easy, but neither of us expected it to be.

I stood back and studied Ron\'s whiteboard, satisfied but annoyed with
myself. \"I should have thought to do this earlier.\"

He shook his head solemnly. \"Wrong. You should have asked for help
earlier.\"

---

[[Full_Text/Chapter_50_Full|← Chapter 50 Full]] | [[Chapter 51 Full|📋 Summary]] | [[Full_Text/Chapter_52_Full|Chapter 52 Full →]]