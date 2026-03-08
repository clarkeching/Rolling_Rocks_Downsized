# Chapter 41 - Full Text

**Current Date:** Monday, September 25th *(continued)*

---

[[Chapter 41 Full|← Back to Chapter 41 Summary]]

---

Chapter 41
==========

Kelvin Park sits in the middle of Watt\'s Bridge City, occupying twenty
acres of prime real estate all protected by royal decree. Kelvin\'s
Peak, an extinct volcanic cone named after Lord Kelvin, the great
scientist who laid the first transatlantic telegraph cable, among other
things, sits in the middle of the park. It was quiet when I reached the
peak, but it would soon fill up with tourists and school kids, and in
the early afternoon, office workers taking exercise and lunch.

I carried two cups of takeout coffee with me, and I settled on a park
bench and sipped mine while I waited for Phil.

I tried to figure out where our bottleneck was. Craig, in his email,
described our project as a \"test-processing factory,\" which was a fair
description of any project in its testing phase. Our testers transformed
our specifications into test scenarios, which they then executed.
Developers fixed failing tests, which were retested. When all of the
test scenarios in the current batch were done, we said the chunk was
GETS. If we had enough GETS software by December 1st then we would ship
it. The question was, which one of our factory\'s machines---the
testers, analysts, developers, managers---was the bottleneck? Or was it
somewhere or someone else?

Phil arrived before I finished my coffee, effortlessly jogging to the
same peak I\'d just slogged my way up to. He wore a T-shirt that read
\"I wish I could change the world, but they won\'t give me the source
code.\" We politely insulted each other (as men in this part of the
world do to demonstrate friendship) while he warmed down. He soon sat,
and I brought him up to date on my discussion with Cheryl.

\"You want me to sit atop of a hill on a beautiful sunny morning and
chat about management theory? Why not! But first things first. Is that
coffee down there mine?\"

I passed it to him.

\"Hmm. It\'s warm -- ish,\" He took a sip and smiled. \"And free. How
can I help?\"

\"Well, first off, do you think the bottleneck concept applies to us?\"

\"Why wouldn\'t it?\"

I said that---obviously---FPP was a project, not a factory, nor an
accounts department, nor a restaurant. They were very different
environments with different types of people working in them. Factories
and restaurants both have many physical things flowing through them, but
the stuff that flows through software projects is \"soft,\" if not
invisible: emails and printouts containing knowledge and ideas; code
made up of databases and source code; bits and bytes, not atoms.

Phil pulled a light jacket from his backpack and put it on. \"None of
that matters. It\'s still about information flow and processes. We must
have a bottleneck.\"

I said, \"I reckon we\'ve got five choices: analysts, testers,
developers, managers or customers. One of them must have less capacity
relative to all the others.\"

\"Agreed, though it could also be our build machines or our test
environments. Now zip it old man, and let me think.\"

And that\'s what he did. He sat back, closed his eyes, and thought. And
then he thought some more. And then, I assume, some more.

Me? I enjoyed the view. I could see the boundaries of the entire city.
Mountains in the east, the river and toll bridge in the northwest; the
Castle defending its own peak in the southwest corner of the park. Just
in front of me, the peak fell away into a cliff. Sports fields, a
running track, and tennis courts sat below the cliff. Tourist trams
circled the park\'s perimeter. They were, the tourist pamphlets said, a
reminder of days gone by.

Phil cleared his throat. \"Okay, I\'ve just run a few thought
experiments assuming that, by some miracle, we added more people to each
role. I then asked myself if the project ran any faster. And for three
of the roles, it didn\'t.\"

\"Ah ha.\"

\"Analysts aren\'t our bottleneck. Most of our analysis is already done,
and the analysts even have spare capacity to help with testing. It\'s
not our customers either, for much the same reasons. And, I\'ll tell you
for free that we ain\'t got no shortage of managers.\"

\"Charming,\" I said. \"So, that leaves the developers or the testers.\"

\"Yep. That\'s where I\'m stuck. If we added more testers, we would
execute more tests and identify more defects, right? But finding defects
sooner doesn\'t get us to December 1st any quicker unless we can fix
them too. I can\'t decide whether we\'d fix the new defects or whether
they\'d just build up because we didn\'t have enough developers.\"

I said, \"If we can fix defects faster than we find them, then our
testers are the bottleneck, otherwise, it\'s the developers.\"

\"Ah ha.\" He held up a single finger to shush me and disappeared into
thought for another couple minutes.

\"I know where our bottleneck used to be,\" he said.

\"Used to be?\"

\"In our first chunk, it was definitely our developers. We found dozens
of defects, but we could only fix a fraction of them. Developers were
definitely our bottleneck then. But things have changed. Now we\'re
fixing defects at about the same rate we can find them. We see that in
Tim\'s daily testing reports.\"

\"So, we have two bottlenecks? Testers and developers.\"

\"Yeah. I think so.\"

Damn. I knew our situation was more complicated than an accounting
department or a cafeteria.

\"Would you say the testers are currently finding it harder to find new
defects than they did a few weeks ago?\" Phil asked.

\"According to Tim\'s testing reports, they are.\"

\"Have you noticed if the newer defects are easier to fix, compared to
those we found a few weeks ago?

I shook my head and shrugged. I wasn\'t close enough to the work to
know.

\"Trust me, they are. Soon, we\'ll be able to fix defects faster than we
can find them and retest them. I\'m sure of that.\"

\"Our testers will soon become our bottleneck?\" We were transitioning
between the two states, like water turning to ice.

He went quiet for a few seconds. \"No, no, no. It\'s worse than I
thought. The testers are about to get a whole lot busier than we ever
expected.\"

I flinched. \"You think they\'re going to unearth more bugs?\"

\"No. But each day that goes by they\'ll have to do more regression
testing.\"

\"Damn. You\'re right.\" Regression testing is when we check we haven\'t
broken anything while changing our software. It was an obvious overhead
cost of doing more, smaller batches, and the overhead increased with
every new batch. I shook my head, embarrassed. \"I should have thought
of it.\"

Phil said, \"It doesn\'t matter. Our regression effort is about to
explode. Testing is about to become our bottleneck.\"

\"This sucks.\"

His eyes widened. \"It doesn\'t suck! This is awesome. If we can squeeze
a twenty percent improvement out of testing, then our entire project
runs twenty percent faster. Our entire project! That\'s brilliant news.
We now know where to focus, so we\'re not only going to get faster, but
we just got wiser too!\"

I nodded, though I didn\'t share his enthusiasm. \"I guess. Rather than
figure out how to make everyone more efficient, we only need to figure
out how to make our testers more efficient.\"

\"It\'s more than that, Steve. I need to slow my developers down, so
they run at the same speed as the testers. We can\'t have them running
out ahead.\"

\"What? Seriously?\"

\"Seriously!\"

I should my head, incredulous. \"You want the developers to just sit
around doing nothing?\"

He shrugged in a don\'t-shoot-the-messenger way. \"Would you prefer we
keep them fixing bugs, even though we don\'t have the capacity to retest
them? All that will do is build up a pile of half-done work. It won\'t
make us go any faster. And we cannot ship untested defects, unless you
suddenly want to start producing non-GETS software? Tell me you don\'t
want that.\"

\"I won\'t do that.\" I shook my head. \"But I also don\'t want our
expensive developers sitting around doing nothing.\"

\"We might have to release some of them back into the developer pool.\"

\"No way.\"

\"Well, we\'d best find something else for them to do then.\"

Neither of us spoke for a minute. Thinking.

I broke the silence with an awkward question. \"Are you willing to let
your developers do testing?\"

\"They already do a lot of testing, lots and lots of testing.\"

\"I don\'t mean normal developer testing. I mean would you let them work
as part of the test team, following the test team\'s rules?\"

He blanched. \"No.\"

\"You\'d rather they sit on their hands and do nothing?\"

He shook his head. \"I\'d rather we use their developer brains rather
than their fingertips.\"

\"Doing what?\"

\"I\'m not sure. Maybe they can automate some things that make the
testers more productive.\" He shrugged. \"I\'ll need to talk to my guys,
and to Tim and his guys too.\"

As we walked back to the office, we agreed the obvious thing to do was
to eliminate, or reduce, anything that wasted tester time. Cancelling
all non-essential meetings was a no-brainer, but Phil also thought we
could reduce testers\' waiting time by doing code builds more
frequently. The build schedule was set up to minimize his developers\'
downtime, but his team could change things so the testers\' downtime was
minimized instead, even if it meant his developers were less productive.

When we hit High Street, I asked him if he knew about how Krzysztof,
Sharon and Brian talked about their test scenarios before executing
their tests. I\'d been so busy with Gregor that I hadn\'t had a chance
to share what they did. I explained, and he agreed that we should get
the other teams working that way.

I told him how Eleanor had berated me in front of Craig and my junior
staff.

\"Ouch.\"

\"It does make me wonder if the other teams have also come up with good
ideas they haven\'t shared yet. We\'ve changed their way of working
significantly, and they\'re bound to have adapted their working
practices.\"

\"I\'ll ask around.\"

When we reached the office, Phil went to talk to Tim and I went to talk
to Catherine and Gregor. We agreed to meet up again later today, before
lunch.

---

[[Full_Text/Chapter_40_Full|← Chapter 40 Full]] | [[Chapter 41 Full|📋 Summary]] | [[Full_Text/Chapter_42_Full|Chapter 42 Full →]]