# Chapter 29 - Full Text

**Current Date:** Wednesday, August 16th *(continued)*

---

[[Chapter 29 Full|← Back to Chapter 29 Summary]]

---

Chapter 29
==========

I mentally searched for an example of some of the requirements---I found
it hard not to use that word---we\'d cut.

\"Originally we had several mechanisms for paying money to FPP\'s
customers. The default method uses the standard inter-bank transfer
mechanism. It\'s cheap and very easy to implement, and mandatory.
Originally, Catherine\'s team required we be able to pay using three
other methods: by check, by instant payment to their U.K. bank account,
and by telegraphic transfer to an overseas account. Catherine chopped
those three methods out.\"

He raised his eyebrows, confused. \"But surely your team already built
those features?\"

\"Built, but not yet tested. They were much harder, more time consuming,
and more expensive to test than the basic option. We spent a lot of time
building them, but because they\'re more complicated we will save a lot
of time now that we don\'t have to test them.\"

\"So you\'re throwing them away? Tossing them, just like Cheryl did with
her unsold product at the end of each meal? \"

I nodded. I waited for him to tell me that was called overproduction,
but he didn\'t.

Craig frowned and rubbed his chin. \"And by cutting those features,
won\'t that make it harder to sell FPP? Won\'t you lose customers since
the product has less features?\"

\"Hardly,\" I said, smiling at the madness of it all. \"We descoped the
less important features. Those features look good on a product
specification sheet, but very, very few customers were ever likely to
want them. Catherine said early on that we\'d definitely never offer the
option to pay by check.

\"But why on earth would she require that feature in the first place if
they\'re not all that valuable?\"

\"Scarcity.\"

He looked at me as if I were crazy. \"Scarcity?\"

\"IT resource is a scarce resource. I\'ve got a four-year-long backlog
of projects waiting to be started. Whenever a new project starts, the
project\'s customers know that they\'ll only ever get one shot at
getting the project right, that it will be years until they get another
wedge of IT resource to enhance it, so what do they do? They ask us to
build every feature they can possibly think of---even if they don\'t
think they\'ll ever use it.\"

\"So the FPP developers built a check payment mechanism on the
off-chance that maybe one day they needed a check payment mechanism?\"

\"Exactly. My eldest daughter does the same with roasted potatoes. She
loves them and she worries there won\'t be enough; she used to pile them
onto her plate, hoarding them, just in case. We stopped her doing that
and asked her to just take more later, if she wants them.\"

Craig half-laughed, half-snorted. \"Ha! She now takes them in smaller
batches, based on her actual demand?\"

My jaw fell open. \"Oh, yes. Smaller batches.\"

\"If it was so easy to stop your daughter\'s hoarding, why haven\'t you
stopped your customers hoarding? Surely everyone knows it happens?\"

\"Everyone does know, and if I had my way, I\'d force each of my
projects\' sponsors to rank each project\'s features and requirements,
like Catherine did in our war room. Then I\'d chop fifty percent of them
before we even started the project. If we got lucky and finished early,
then they could either go live early and we could start the next project
on our big backlog, or we could use the time to layer on some of the
lower value features.\"

\"Okay, I get that. It\'s a bit like buying a basic model of a car, then
choosing to add on extras if you had the budget,\" he sounded almost
grumpy. \"But why don\'t you insist that your customers prioritize at
the start?\"

\"I\'ve tried, but our customers insist that every single feature is top
priority and therefore mandatory.\" I nodded towards the thick
requirement folder. \"And yet, in a crisis, it took less than four hours
to strip those three hundred pages down to one hundred.\"

I paused, then added, \"Hoarding is one cause of overproduction. Another
is that our customers know, at the start of their project, that later on
they\'ll be asked to chop out features, so they add stuff that they
don\'t really want in order to protect the features they do want.\"

\"Packing peanuts."

"Pardon?"

"They\'re like those foam peanuts businesses fill packages with so the
goods they\'re shipping don\'t move around in transit."

"I suppose."

"Now, tell me, what\'s the equivalent of underproduction?\"

It only took me a moment to figure it out. \"Change requests.\"

\"Explain.\"

I spoke slowly as I carefully considered my words. \"Underproduction
happens when we don\'t build something our customer wants. We don\'t
build it, because---to use your words---we didn\'t forecast it at the
start of the project. In my words, a requirement is wrong, so our
customers ask us to change it, or a requirement is missing, so they ask
us to add it.\"

I told him about FPP\'s Customer Level Income change request, the one I
heard about in Gregor\'s management meeting just before I announced the
FPP emergency. It stuck in my mind clearly. I even remembered its CR
number: 191. It was a typical example.

He said, \"And your customers really wanted it? They weren\'t just
negotiating with you, playing some game?\"

\"Catherine said it was a real money-spinner.\"

\"So why was it rejected?\"

\"Simple. Change requests take a lot of extra work, and they mostly
happen near the end of the project when it\'s harder to change the code
and we\'re usually already behind schedule. They chew up any contingency
hidden in our plans and make us deliver late.\"

He said, \"In the cafeteria, they lost sales and disappointed their
customers when they didn\'t cook enough of a popular dish. In the old
days, they had no ability to change their forecasted menu after 9 a.m.\"

I picked the requirements document up off the table and leafed through
the pages. \"There\'s some good research out there on this, Craig, and
for medium to large projects, on average, we could expect a quarter to a
third of the requirements in this document to be changed during the
duration of the project.\"

\"So what\'s that? Between seventy-five and a hundred of the original
three hundred pages?\"

\"Uh-huh. And those are only the changes that get approved. We reject
many more than that.\"

\"And I bet your customers know that and only ask for the most important
changes.\"

\"Of course.\"

Craig leaned forward, then said in a soft voice. \"I\'ve got some good
news and some bad news.\"

I leaned forward. \"What\'s the bad news?\" Though I knew what was
coming.

\"The bad news is that I have a wedding rehearsal to go to. I need to
leave very soon or my son\'s wedding rehearsal will be ruined and his
new mother-in-law will end up in jail for murdering me.\"

\"And then you\'re not back in the office for another three weeks.\"

He nodded. \"But I have two pieces of good news. First, I will give you
some homework and then meet you here very early tomorrow morning to
review it. Second, you have all the pieces of the jigsaw in your brain,
and I am certain you can solve this problem.\"

I shook my head. \"I seriously doubt that.\"

He ignored me and stood up. \"I need to call my son, let him know I\'m
on my way. While I\'m gone, can you draw a conflict cloud for change
requests?\"

\"You\'re kidding?\"

He pulled out his phone and walked away.

I sulked for a minute, feeling sorry for myself, then pulled out my pen
and ripped a piece of paper from the requirements folder. Turning the
page over to the blank side, I imagined the stick-man shape and drew the
five boxes. I filled out the D and D\' boxes easily---change vs. don\'t
change---then I jotted down the pros and cons for each side, filled in
the B and C boxes, and then the A box. It took just a few minutes.

![An
Image](media/rId6.png)

Craig soon returned, still talking on his phone, and found me winning a
game of solitaire on Camilla. (Fran used to call my phone that because
sometimes, she said, it was like there were three of us in our
relationship.) I felt tired.

He stood in front of me, looked down, and then said to the person on the
phone, \"I\'ll ask him.\" He placed his hand over the microphone.
\"Eleanor wants to know how we\'re getting along. What shall I tell
her?\"

\"Like old friends.\"

He repeated my words then hung up and sat down. I pushed the cloud
towards him. He read it once silently, and then once more out loud.

\"In order to have a commercially successful product, we must make a
good product. In order to make a good product, we must approve change
requests. In order to have a commercially successful product, we must
deliver on time. In order to deliver on time, we must not approve change
requests. Norbert said you were a quick learner.\"

I ignored the compliment. \"How does this help me? I can\'t approve any
change requests in FPP.\"

\"Why not?\"

I gasped. What a stupid question. \"The only thing the FPP team will be
doing between now and December is finding and fixing defects. We\'ll
squeeze in as many rounds of testing as we can, but even then we will
ship a shoddy product. Changes are a luxury we can\'t afford. We\'ve
already discussed this.\"

\"Will you have any room to do change requests after December 1st?\"

I shook my head. \"Assuming we ship on time, we\'ll still have to spend
several months fixing bugs. We won\'t have many customers, so while
it\'s not ideal, it\'s tolerable.\"

\"Steve, you\'re forgetting one thing.\"

\"What?\"

\"The sad picture you\'ve just painted is what you were going to do
before we started talking. But things are different now. You have the
pieces of the jigsaw puzzle in your head, and when you snap them
together, you\'ll see a different picture.\"

More word games, but I played along. \"What are the pieces of the
puzzle?\"

\"You tell me.\"

"I don\'t even know what the picture on the puzzle box looks like."

"Tell me what Cheryl did."

So I listed off the ideas Cheryl had applied to her own problem.

I started with three ideas we were already using: testing defects out at
the end (which was expensive but better than no testing) and in-process
inspections and in-process testing.

Then I listed the new pieces of the jigsaw: *small batches*,
*prioritizing requirements*, and finally, *building to demand*, not to
forecast.

Craig said, \"Now, tell me what the picture on the new jigsaw box should
look like.\"

\"I ship a good quality product on December 1st. Good quality as in low
defects and our customers like it.\"

He said, \"I know I\'ve thrown a lot at you in the last few hours, but
here\'s one piece of the jigsaw you might not figure out because it\'s
counterintuitive: Sacrificing quality almost always slows things down.\"

I raised my eyebrows and rolled my eyes, just a little, in an
easy-for-you-to-say kind of way.

He smiled. \"You should look happier.\"

\"Should I?\"

\"You\'ve already identified your first two slightly smaller batches.\"

I studied his face, trying to tell if he was joking or not. I decided he
wasn\'t. \"I have?\"

He said, \"What date does your first batch end on?\"

I had no idea. We\'d only mentioned one date in our entire conversation,
as far as I could recall and ... Oh ... my ... god.

\"My first batch ends on December 1st!\" ---he nodded, my eyes
widened---\"And ... the second starts immediately afterwards!\"

Snap! The construction of my jigsaw began. Was it as simple as that:
thinking of a big project as a series of small projects?

He grinned. \"Your homework---draw the overproduction cloud; review the
cloud you drew when we first met; draw more clouds, if it helps. You\'ll
find drawing the hands easy enough, but the shoulders will challenge
you. You need them, though, so persevere, even if they make you think.
Once you\'ve done your clouds, then think about small batches.\"

\"Okay.\"

\"I will meet you here at 5:30 tomorrow for an impossibly early
breakfast. Okay?\"

I said *Okay* again, but more out of habit than anything else. My head
hurt.

---

[[Full_Text/Chapter_28_Full|← Chapter 28 Full]] | [[Chapter 29 Full|📋 Summary]] | [[Full_Text/Chapter_30_Full|Chapter 30 Full →]]