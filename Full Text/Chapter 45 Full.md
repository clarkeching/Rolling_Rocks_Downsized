# Chapter 45 - Full Text

**Current Date:** Monday, September 25th *(continued)*

---

[[Chapter 45 Full|← Back to Chapter 45 Summary]]

---

Chapter 45
==========

I arrived at the conference room at exactly 11 a.m. Phil and Tim were
already there. Phil had tied a knot in Fippy the Snake\'s tail and was
making *yee-ha* noises as he twirled him over his head like a lasso.

We sat and I told them about Catherine\'s descoping of the search
features.

Phil said, \"What stopped her doing that months ago?\"

I said, \"Maybe she wasn\'t desperate enough? Plus, last time we
descoped we asked her to prioritize features. But this time, with the
search feature, she\'s trimmed a five-star solution for an existing
feature down to a one-star solution.\"

Phil said, \"Whatever the reason, that\'s awesome news let\'s hope she
keeps slashing. But now, on to more important and---dare I say
it?---more interesting things!\" He rested Fippy on the table. \"We
haven\'t had a lot of time, but Tim and I have come up with a few ways
to increase our testing capacity quickly, none of which involve chucking
more testers at the problem or lowering quality. Some of our ideas are
obvious, some of them are ... not quite so obvious.\"

Tim said, \"Let\'s start with the four most obvious ideas. First, we\'ll
cut unnecessary and over-long meetings. Second, we\'ll rollout Kryz,
Sharon and Brian\'s pre-test discussion to all the other teams.
Third---\"

I said, \"You heard about that?\"

\"Yeah,\" he said, then averted his gaze for a moment. \"Sharon updated
me on Friday afternoon. Third, we will start doing a little look ahead
and batching up some tests. Fourth, we will---\"

\"Hang on,\" I said. \"You want to increase the batch size? Isn\'t that
the exact opposite of what we want to do?\"

Tim shook his head. \"I shouldn\'t think so. Not if it makes our
bottleneck team faster. It\'s often quicker to execute tests A, B and C
together as one batch, rather than do each in isolation. Why? Because
the output of A is the input to B, and so on. Make sense?\"

I checked with Phil, who nodded. \"We\'re not talking about doing bigger
batches, just selecting what we work on now so it makes more efficient
use of the tester\'s time.\"

\"Okay.\"

\"And fourth, we will stop our developers from batching up their fixes.
Rather than dumping a batch of, say, twenty fixes every third day, we
want them to drip feed the fixes, for retesting, several times a day.\"

\"Phil mentioned this possibility,\" I said.

Tim said, \"Developers are non-bottlenecks, so by definition they have
spare capacity. We should use that spare capacity to do more releases.
More releases will improve the flow of work to the testing team and
it\'ll keep the testers busy. As it is, they are often blocked while
they wait for fixes to be released.\"

\"Also,\" Phil said, \"if we drip feed the defects rather than releasing
twenty fixes in one burst, then the test guys can get cleverer and more
focused about their regression testing.\"

I said, \"Makes sense, but I have one concern. More releases will
require more coordination between the teams, right?\"

\"Yes, we will have more releases so we\'ll have to coordinate those
more carefully. But, equally, each release will be much smaller so they
should be easier to coordinate.\"

\"Okay.\"

Phil waited a moment to see if I had any more questions, then said,
\"Now for the less obvious suggestions. Prepare yourself to be
shocked.\"

I made a show of pretending to brace myself.

Tim sat upright in his chair before he spoke. \"This *will* shock you,
Steve. I promise you. But it seems like a good idea.\"

I smiled politely, humoring him. \"I\'m ready.\"

\"It pains me, but we should temporarily disband FPP\'s automated
testing team.\"

I raised my eyebrows, shook my head, and dropped my jaw---all at the
same time. It\'s possible some drool dripped out the side of my mouth.
He was kidding me, right? That team automated much of the testing that
would otherwise be done manually. They created a bunch of incredibly
cheap, reliable, digital robots who tapped away at FPP\'s software
making sure it worked as defined, much like our manual testers did, but
they did it in the middle of the night and without bio breaks or
complaining. Tim had fought hard to form and protect the team. But now,
here he was, offering to close it down.

\"Surely we need more automated testing now, not less?\"

\"Yes, but right now, we\'re doing the wrong sort of automated testing.
We\'re still creating FPP, so its user interface keeps changing,
sometimes a dozen times a day, and since our automated tests work
through the user interface, they keep breaking. Accordingly, I\'ve got
my four most skilled and knowledgeable testers working full-time fixing
broken test scripts. I\'d rather we abandon the tests temporarily, since
they\'re basically useless, then fix them later, when the UI
stabilizes.\"

I nodded slowly, considering what he\'d just said. \"We\'d increase our
manual test capacity from twenty to twenty-four, which is at least a
twenty percent increase.\" Nice.

\"No, Phil and I think we can use those guys more cleverly than that,\"
Tim said.

Phil said, \"We\'ve got a better idea. Actually, there\'s a word for
it ...\" But then he stopped talking because he couldn\'t think of the
word. \"It\'s the phenomenon of when you add one plus one and get
three.\"

\"Synergy?\"

\"That\'s it. We want to pair each freed-up tester with a developer and
use the synergy of their combined tester and developer brain power.
Developers know and can do and see stuff that testers can\'t. Testers
know and can do and see stuff that developers can\'t. We\'ve not had a
lot of time to think about this, but we\'ve already thought of three
ways we can get synergy by getting testers and developers working
together.\"

\"Tell me more.\"

Tim said, \"Here\'s the first one. My testers understand the data and
the application better than the developers, but Phil\'s developers
understand the code. We want to pair two of them up and automate the
creation of some of our most useful test data.\"

I nodded.

\"Our data-setup team\'s work is manual and a little error-prone. If we
automate some of their work then we could use some of the folk on that
team to do manual testing.\"

Phil said, \"We\'ll start with the low-hanging fruit---the most common
tasks that take the most time when done manually---and can have the
first of them automated within a couple of days.\"

\"That\'s \... ambitious. Are you sure?\"

Phil\'s face reddened a little. \"Yeah \... well, see, a good bit of the
code is already built. Me and my developers, we\'re lazy, so we automate
time-consuming and repetitive stuff, like data setup, whenever we can.
It\'s just what we do. We just never thought to share our hand-cranked
tools with Tim\'s team.\"

\"To be fair, we never asked,\" Tim said. \"That should free up maybe
three to five data-setup staff to execute manual regression tests.\"

\"How much extra test capacity will that give us?\"

Tim screwed up his face. \"Maybe ten or twenty percent? The people we
free up aren\'t our strongest testers, but they can do some of the
easier stuff, which will free up the more skilled guys to do the harder
stuff.\"

I nodded with what I hoped looked like a serious look on my face.
Secretly though, on the inside I was dancing. Ten percent extra
bottleneck capacity made the entire project run ten percent faster.
\"Okay. You said there were three examples of synergy. What\'s next?\"

\"This one is something we probably should have done from the start of
the project,\" Phil said. \"We want to pair up another tester and
developer and automate the testing of FPP\'s calculation engine.\"

Tim said, \"It takes up a lot of my team\'s time, is painfully
error-prone and none of them like it.\"

I nodded. The calculation engine was the most important bit of the
entire solution to get right.

Phil said, \"But since it\'s an algorithm, with inputs and expected
outputs, it\'s straight-forward to automate. If Tim\'s team prepares a
spreadsheet table of inputs and expected results, we\'ll create a test
harness which hooks directly into the calculation engine. We will run
several days\' worth of manual testing in several minutes, several times
a day if we want.\"

I saw a red flag. \"Why will this work, when the UI-based automation
doesn\'t?\"

Phil smiled. \"The calcs are stable, the user interface isn\'t. Plus,
we\'ll hook the testing harness directly into the depths of the code,
totally avoiding the UI. The UI can keep changing, but it won\'t affect
our tests.\"

\"Okay,\" I said. \"And let me guess. You already have a test harness in
place which you can share with the testers for free?\"

\"Nope. But we can build one quickly.\"

\"Good. And the third?\"

\"You know how, until recently, our two teams have worked separately?\"
Tim said. \"Well, working separately resulted in some duplicated
testing. We think we can eliminate some of that now that we are working
together.\"

\"What? Why on earth would we do duplicate testing at all?\"

\"When a developer fixes a defect, they do their own testing and then
hand it over to my testers who do *their* own testing. They assume the
developer has done a good job, but they start with a blank slate. So,
sometimes the testers repeat some testing the developers have already
done. When they worked separately that made sense, but now we can remove
some of the overlap.\"

\"Okay,\" I said. \"Are you sure you can do this without cutting
corners?\"

Tim\'s eyes narrowed and I realized I\'d inadvertently questioned his
and his team\'s professionalism. They\'d never suggest anything they
thought jeopardized quality. I tried to recover from my misstep.
\"So \... do you think we could, maybe, trial this with Kryz, Sharon and
Brian\'s team before rolling it out to the other teams?\"

Tim said, \"Of course.\"

I nodded. \"How much extra testing capacity will this create?\"

Tim said, \"My gut says between ten and thirty percent, so, say twenty
percent?\"

I said, \"I\'ll assume ten. Anything else?\"

Tim said, \"Not yet. But this is surely enough to get us started.\"

I thought a moment. \"It\'s a good start.\" Which it was, but I knew it
wasn\'t enough.

I knew I needed to be pessimistic about the potential, but I figured
their changes would give us at least fifty percent improvement in
test-team throughput, which meant the whole team would run fifty percent
faster. Though we could well get considerably more.

That leap in performance seemed both outrageous and conservative at the
same time. Outrageous because, normally, we viewed a fifteen percent
improvement as impressive; conservative because I\'d consciously rounded
down. We still had two ex-UI automation testers up our sleeves and the
three of us had only spent a few hours thinking about this. I knew our
teams would come up with more innovations, over time, though we
couldn\'t afford to overwhelm ourselves with too many changes at once.

I frowned, \"You know, all of these suggestions seem really smart and
achievable, but if they\'re so smart, how come we\'ve never done them
before?\"

Tim shrugged. \"We never knew we had a bottleneck before, so previously
we tried to keep both our teams running as fast as they could. That, I
guess, was suboptimal, because sometimes improvements in one team
deteriorated performance in another.\"

Phil said, \"Now that we know we have a bottleneck, we know we have to
manage things differently; to look at the whole, not just the parts.\"

\"Okay,\" I said. \"Now I have a suggestion. What do you call the person
who sits at the back of the boat in those rowing boat races, the ones
between Cambridge and Oxford University?\"

Phil said, \"The one they throw in the water at the end of a regatta?\"

\"Yeah.\"

\"It\'s the coxswain. I think.\"

\"That\'s the one,\" I said. \"We need to get ourselves some
coxswains.\"

Neither spoke.

\"The coxswain adds weight and doesn\'t row. Right? So why have them?\"

Phil said, \"They steer, don\'t they?\"

I nodded.

\"And they keep the individual rowers rowing in sync,\" Tim added.

I said, \"And they also provide a bit of motivation by keeping the
pressure on.\"

Phil looked doubtful. \"And you think we to need get ourselves some
coxswains? To do the coordination work?\"

I nodded.

\"Don\'t Tim, Anne and I already do that?\"

I said, \"Sort of. You manage the staff in your specialties, and that
worked fine before. But now that the teams are multi-functional and
collaborate much more, we need someone in each team who coordinates the
work of the team.\"

Tim said, \"Like mini-project managers?\"

I nodded. \"Like that, but focusing on the internal working of the team,
rather than the external stuff. Gregor does all the external stuff, but
doesn\'t have enough time to coordinate all the work inside the teams.\"
I thought a moment, then added, \"And if he did, it\'d look like he was
micro-managing.\"

Tim said, \"Some of the teams are struggling. There\'s a lot more
coordination required than they\'re used to.\"

Phil said, \"Yeah, but others are doing okay.\"

\"Why is that?\"

He shrugged. \"I guess some teams just got lucky and ended up with a
self-appointed coordinator inside the team. Some people are just
naturally good at that sort of stuff and they can\'t help themselves.\"

I said, \"So maybe we need to recognize those people for what they\'re
already doing and then figure out how to help the other teams do the
same? They might have someone in the team who just needs permission to
take on the coxswain work. Or we might need to provide someone.\"

Phil said, \"I buy all that, except for one thing. We need to find a
better name than coxswain.\"

We spent a minute discussing possible names for the role. I decided to
steal Craig Lally\'s job title and call them flowmasters.

With that settled, Tim and Phil agreed they\'d get together with Gregor
and Anne to choose the new flowmasters and to figure out what the job
entailed and offer coaching.

I excused myself, leaving the other two to start rolling out our
changes, and returned to my office, hoping that Catherine had managed to
thin the product out even further.

---

[[Full_Text/Chapter_44_Full|← Chapter 44 Full]] | [[Chapter 45 Full|📋 Summary]] | [[Full_Text/Chapter_46_Full|Chapter 46 Full →]]