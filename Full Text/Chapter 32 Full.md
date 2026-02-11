# Chapter 32 - Full Text

**Current Date:** Wednesday, August 16th *(continued)*

---

[[Chapter 32 Full|← Back to Chapter 32 Summary]]

---

Chapter 32
==========

I went to the lounge looking for any nomad dishes in need of a good
cleaning and found two bowls the kids had left there after their supper.
One was empty, the other half-full of soggy cornflakes. That would be my
little Ashley---she always took more cereal than she needed, then we
ended up wasting it. I\'d asked her, many times, to just take a small
bowl\'s worth of cereal then get more if she was still hungry, but she
was still young.

I took them and an apple core I found on a side table back through to
the kitchen.

I threw the apple core in our small compost bin, then washed the bowls
and started on my next batch of washing. As I started scrubbing the
frying pan, my mind soon turned to requirements, or *forecasts*, as
Craig called them.

I\'d had a few hours to cogitate on that thought, and finally I felt
primed and ready to tackle the topic consciously. I decided he was
rightish: Some requirements were required, but some were optional and
some were guesses.

In our War Room, Catherine had already pared FPP back to the bare bones
requirements. She said we couldn\'t go live without them, and I believed
her. The default payment method I\'d told Craig about, which used the
United Kingdom\'s standard inter-bank transfer mechanism, was a good
example. It was indisputably required because no one would buy the
product if we didn\'t offer it. They were like French fries in the
cafeteria.

But what about the other three payment methods she had descoped as well?
They were optional, and when push came to shove, Catherine had pushed
and shoved them aside. But it didn\'t make sense to call them *optional
requirements*. That was an oxymoron, wasn\'t it? I needed a better word
than requirements, but there were too many to choose from: solutions,
designs, features, behaviors, functions, use cases ...

I flipped a coin in my head, and before it landed I\'d decided to call
them features. I imagined a conversation with a customer:

*Me: We\'ve built these features already.*

*Customer: Good. What about those other features?*

*Me: We haven\'t built them yet.*

The word seemed to fit.

I paused for a moment and realized that I\'d been so caught up in
thinking that I\'d stopped cleaning up. I poured some more hot water
into the sink and started again.

So, there were four payment method features, one of them required, three
optional. But here\'s where things got interesting: They weren\'t
equally optional.

Of those three optional payment methods---check, instant payment to a
U.K. bank account, and telegraphic transfer to an overseas account---the
first, paying by check was optional and very low priority. Wyx-Fin
stopped sending check payments out years earlier. It was probably
included at the start of the project so that customers wise to the way
of projects could look suitably pained when they agreed they could live
without it during some descoping exercise. It was filler, like a
bodyguard, willing to throw itself in front of a bullet to save the rich
guy.

The instant payment feature was optional, but it wasn\'t just filler.
Wealthier customers, the ones we wanted to attract, would prefer to use
it for unusually large and urgent, one-off payments. It wasn\'t
required, but I imagine Catherine would have kept it in if she possibly
could have. So, it was optional and either high or medium priority.

The telegraphic transfer was the most interesting of the three. It would
appeal to potential customers who would retire to Spain, say, to avoid
rickets and scurvy in their later years. They would be a small subset of
our wealthier and most profitable customers, and it might help our
overall sales. Or it might not. We wouldn\'t know until we tried to sell
it. Of the four options, it most resembled a forecast. Its value was
uncertain. If there were a phase two and we discovered demand for it,
then we would build it to fill that gap.

I stopped and smiled to myself. I felt like I\'d just realized what I\'d
subconsciously known all along.

I gave the pan an angry scrub. It annoyed me that my customers always
claimed that every feature was required, when logic said they were not.

I stopped cleaning for a moment as the obvious occurred to me. If we
could get our customers to prioritize honestly, then we could reduce
hoarding significantly and free up scarce IT capacity. If we created
more IT capacity, we\'d be able to create space that would reduce the
need to hoard. I guess we\'d call that a *virtuous* circle.

In fact, if we could just guarantee that each project had a phase two,
then we\'d be halfway there. But, of course, what customer in their
right mind would believe that guarantee?

I grabbed another pot from the stove, dunked it in the hot soapy water
and started scrubbing. Mom had used this pot to make tomorrow morning\'s
porridge, and even though she\'d soaked it, the inside base was thick
with stuck-on porridge. Ick.

As I scrubbed the pot, I realized that the word *features* didn\'t quite
cut it. We also had some non-functional requirements---that is,
requirements that were not features. They were things like security and
performance and scalability---the kinds of things you measured on a
scale and could have more or less of. You could have faster
performance---at a price---and you could have high levels of
security---also at a price. And you could build a system so it was
easier, or harder, to scale. So the equivalent of saying that features
were required or optional, when dealing with non-functionals, was the
flexibility of paying for different performance level. It was like
having the option of paying for a three-star hotel or a five-star hotel.
They both provided the same functionality, but you paid more or less for
different levels of quality.

I moved to the non-stick wok and gave it a quick brush and dry. Another
word for non-functional requirements was *qualities*, which was short
for qualities of service. I decided to use that word going forward,
along with features, and forgo the word *requirements* for good.

Was there another way to get our customers to prioritize? It seemed to
be the key.

In the cafeteria\'s kitchen they prioritized by cooking more of what
their customers were buying. I couldn\'t just cook up a batch of
features cheaply and make more if they sold well. That was one way our
two domains were very different.

I\'d told Craig how, if only our customers prioritized their features at
the start of each project, we could build a smallish version of the
solution, just big enough that we could comfortably deliver it before
the delivery date and within budget. Then, if we had time and budget
left over, we could add on their next highest features.

That sounded a lot like cooking up a medium sized batch followed by a
few smaller sized batches. Craig had refused to tell me what small
batches looked like in my environment. He said I\'d figure it out. And,
I thought I just had.

Could working in small batches be something as simple as breaking that
medium sized project down into a bunch of smaller projects? Craig had
grinned when I asked him that question, but not answered.

I thought it could.

Was that all there was to it?

I thought a moment, and decided it was. A small batch was a small
project in which we delivered a small selection of features; not just a
small selection, but a small selection of the most important features.

How disappointingly dull. I\'d expected thunderclaps and awe, or maybe a
Eureka Moment where I jumped out of my office and ran naked down the
street. But there was none of that. Did Cheryl have similar thoughts of
underwhelmed-ness when she figured out she shouldn\'t cook a huge pot of
cabbage, but a few smaller pots? Probably.

Still, it felt right and it felt good. I smiled and told myself out
loud, "Nice."

So, small batches were small projects. But that still didn\'t help me
with the prioritization problem.

Or did it? We couldn\'t get our customers to prioritize adequately when
we did big projects. Would they behave differently if, instead of asking
them to set in stone twelve months of work, we asked them to tell us
what features they needed in the first month? What if we added that our
analysts, designers, developers and testers were ready to start work,
and if they didn\'t tell us what to work on, we\'d choose on their
behalf and start spending their budget? What if we added that we were
most likely to pick the features that were the most technically
interesting, unless they told us otherwise?

Yes. Small batches would force our customers to prioritize.

I let that thought linger ...

I wiped around the benches and the kitchen table and went into the
utility room to grab our broom. I gave the kitchen floor a quick sweep
then emptied the rubbish bin.

Craig was right; small batches were key. But a key is useless without
someone to put it in the lock, turn it, and then yank the door open.

I rushed through to the hallway and grabbed Camilla from my jacket.

---

[[Full_Text/Chapter_31_Full|← Chapter 31 Full]] | [[Chapter 32 Full|📋 Summary]] | [[Full_Text/Chapter_33_Full|Chapter 33 Full →]]