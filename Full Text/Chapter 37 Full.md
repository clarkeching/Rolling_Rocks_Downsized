# Chapter 37 - Full Text

**Current Date:** Friday, September 22nd *(continued)*

---

[[Chapter 37 Full|← Back to Chapter 37 Summary]]

---

Chapter 37
==========

Kryz moved one of the dead cacti from atop the pile of books, folders
and papers it protected and placed it to one side. He rifled through the
pile and pulled an inch-thick ring binder from near the bottom and held
it up for us all to see. I recognized from the cover that it was one of
FPP\'s specification documents. He flipped through the pages then laid
the document open on the table so that Eleanor and I could see it. He
said it was the original specification for the screens he had just shown
Eleanor.

\"This was one of the first features we tested, in the first chunk.
We\'ve just been regression testing it, to check it still works, since
we sometimes accidentally break software when adding something new.\" He
paused to check that Eleanor was paying full attention. \"Now, Eleanor,
I must inform you, lest you think I am incompetent, that I spent many
hours preparing this specification many, many months ago, and it was
reviewed several times and all the right people signed off on it before
Brian here built it. You understand?\"

\"Are you telling me this, Kryz, so that when I see something
not-so-good I will know you did a good job?\"

\"I am. Despite all the effort we put into writing accurate requirements
documents, they still contained a lot of ambiguous requirements, which
result in us finding defects which then needed to be reworked. Okay?\"

She nodded. \"Of course.\"

\"Before I explain what we used to do, and what we now do, I need to
explain some background. When we started delivering GETS software,
Gregor made us all move desks so that we sat in small, focused
test-and-rework teams. He said he wanted to get rid of the piles of
half-done work that build up between teams that sit separately. Brian,
Sharon and I, we are a team and we now sit together. Previously, Sharon
and all the testers worked on the fourth floor, and Brian and I sat with
our own analyst and developer teams, placed at different ends of the
sixth floor. It was this sitting together that enabled us to discover
our way of finding defects without testing.\"

He paused, as if collecting his thoughts. \"We made our discovery a few
weeks ago, during the first chunk. Sharon has just finished testing this
particular specification.\" He pointed at the page he had unearthed for
us. \"And guess what, Eleanor?\"

Eleanor shook her head. \"I\'ve no idea, Kryz. Tell me.\"

\"She found defects! I told you that already, Eleanor.\"

Eleanor\'s face blanked and she glared at me, annoyed that I\'d wasted
her time. I shrugged my shoulders. She should have stuck to the script.
I glanced at Craig and made what I hoped looked like an apologetic
smile. He smiled back as if to say that he didn\'t mind.

Seemingly oblivious, Kryz continued with his story. \"In fact, she found
lots of defects! But that\'s okay because that\'s why we test things.\"

Eleanor smiled, but it looked to me like the thin veneer of charm she\'d
painted on her face was about to crack.

Kryz smiled back. \"Now, normally, Sharon would just log the defects
into her defect tracking software so that Brian could fix them later,
and then she\'d carry on doing more testing. But, for some reason,
perhaps it was because we were sitting next to each other, Sharon did
something very unusual. She spun around in her chair and tapped us both
on our shoulders. Well, she actually tapped me on the shoulder, and then
Brian, and then the three of us had a good chat about these bugs she had
just found.

\"This is when we made our really interesting discovery. After a bit of
chat, we realized we could have found many of these bugs without Sharon
*actually* doing any testing. And that\'s what we do now. We three talk
about how we expect the software to behave, before we test it, and if we
disagree on how we think the software should behave then that means the
requirements I wrote were probably ambiguous and Brian has probably
built something different than what I intended.\"

I was suddenly intrigued as I sensed, at last, the direction he was
headed. \"Ambiguous requirements, Kryz?\"

\"Yes,\" his eyes grew wide. \"I asked for X, Brian interpreted X
differently than what I intended and wrote software that did Y. It is
very common. The English language is sometimes open to many
interpretations.\"

Eleanor shook her head. \"This doesn\'t make any sense.\"

I explained that ambiguous and vague specifications were very common
causes of rework in software projects all around the world, and that was
why---as Kryz had gone to pains to describe---we spent so much time
trying to get our specs right up front.

\"A lot of good that did you.\" She turned to Kryz. \"Can you give me an
example of ambiguous requirements?\"

He thought a moment then grinned. \"When I started working here, Phil,
who is one of our senior programmers and who likes his coffee very much,
suggested I try the coffee from a little Italian cafe he likes just off
High Street. So I did, and he was right, so I emailed him and said thank
you for his recommendation. He emailed me back and said, \'Good. Once
you try their coffee, you\'ll never go back.\' Which surprised me
because I intended on going back.\"

Eleanor said nothing for a moment, then snarfed (snorted and laughed at
the same time), something I\'ve never heard her do before, nor
thankfully, since. She said, \"I guess, this time, it was my request to
you that was ambiguous. I meant an example of a defect that was caused
by ambiguous requirements.\"

Kryz said, \"Of course.\" He picked up a sheaf of papers from his desk
and flipped through the pages so we could all see. The pages were
covered in red circles, maybe two or three per page. \"This was
something we worked on yesterday. Every red circle is a potential defect
we found when Brian, Sharon and I disagreed about how we expected the
software to behave.\"

He pointed at the first circle. \"You see this one? It requires that
under certain circumstances, the system must pay a refund into the
customer\'s bank account. Seems simple, right? The problem is, the
customer might have more than one bank account set up on our system, and
although I didn\'t write it explicitly, I meant that the refund should
be into the account the original payment came from. When Brian wrote the
code, he assumed the refund should go to the customer\'s default
account. You understand?\"

We nodded.

\"It was only yesterday, when we listed out the scenarios we should test
to prove that the requirement was fulfilled, that we realized it wasn\'t
absolutely clear how the software was supposed to behave. We raised a
bug, and this morning Catherine\'s team decided the code needs to be
changed, which Brian will do today. Then, either today or tomorrow,
Sharon or I will test not only that this scenario works but also that
we\'ve not inadvertently broken anything while fixing it."

Eleanor said, \"I understand now. So you find this type of defect
sooner, by talking and testing that you have a shared understanding,
before you test the actual software. If you disagree about how the
software should behave, then you probably have a defect which then needs
to be fixed.\"

\"That is correct, Eleanor.\"

\"It\'s an awful shame, Kryz, that you didn\'t have those conversations
a long time ago, before the software was built.

He nodded emphatically. \"This project could have prevented a lot of
defects and avoided a lot of rework.\"

Kryz described the next three circled defects before Eleanor put her
hand up to stop him. \"I need a moment to think this through. Please.\"
She looked down at the floor and closed her eyes.

I mouthed \"well done!\" to Kryz and Sharon and Brian, but my pleasure
was brief. A few moments later, Eleanor opened her eyes and turned to
me---though turned *on* me might be a better way of putting it. I
flinched when I saw her face. Her jaw was tight and her eyes had
narrowed in anger.

\"What I simply do not understand,\" she barked at me, \"is why you did
not have these conversations months ago, before you built the
software!\"

I stepped back involuntarily. \"Pardon?\"

\"How much rework could you have prevented if you\'d prevented the
defects in the first place?\"

\"I don\'t know, I ...\"

\"Maybe you could have delivered FPP by now.\"

\"I don\'t ... perhaps ...\"

\"Steven. Right now most of your staff are either fixing or retesting
defects. If only your teams had collaborated and challenged the
requirements before building the software, we\'d have surely shipped FPP
now.\"

I shook my head. \"Maybe ...\"

She ignored me and turned to Craig. \"You manufacturing folk wouldn\'t
ever build something without clearly specifying how to test it first,
would you?\"

He thought a moment before answering. \"We always specify tolerances as
part of specifications. You know: \'the widget has to be ten mm long
plus or minus five thousandths of a mm.\' How else would we set up our
machines? How else would we procure our raw materials? How would we test
the widgets after we\'d created them?\"

Eleanor, her face now completely devoid of charm, said, \"Of course you
do. That\'s one of the ways you build quality in to your processes. Good
carpenters measure twice and cut once too." She turned to me. \"And
Steven, I imagine that even you techies specify how you\'d like your
steak done when you order it, rather than after it\'s cooked. Correct?\"

\"Of course we do. But---\"

\"But nothing. It is clear to me FPP has been delayed considerably
because your team is now busy fixing these requirements defects, many of
which could have been avoided. Why is that? Why didn\'t your analysts,
developers and testers have these conversations earlier?\"

I shook my head as I struggled to find an answer. \"Honestly, best
practice is to keep developers and testers separate. That way, testers
find more defects.\"

\"Is that true, Sharon?\"

Sharon glanced at me then Eleanor, looking nervous that she\'d just
found herself stuck in the middle of an argument between her boss\'s
boss\'s boss and her boss\'s boss\'s boss\'s boss.

\"When we work independently, we come to the software with fresh eyes
and we do tend to find more bugs.\"

\"But that\'s after the software has been built? Correct?\"

\"Yes.\"

\"Wouldn\'t you be better off using your fresh eyes to prevent defects
rather than finding them?\"

Sharon nodded cautiously. \"Though we still couldn\'t prevent all
defects---maybe only half of them.\"

Eleanor nodded assertively, as if the case had been closed. She turned
to Kryz. \"Have you shared your new way of working with anyone else?\"

He said, \"Not yet.\"

Eleanor turned back to me. \"Did you know about this team\'s innovation
before now?\"

I felt my neck redden. \"We\'ve been busy ramping up ...\"

\"So I\'ve just been doing your job for you. Great. Have any of your
other teams come up with good ideas we should know about?\"

I hung my head. \"I don\'t know.\"

And then my public interrogation and humiliation suddenly stopped. Her
arms flopped by her sides and she looked down at the ground. She
muttered, \"What an embarrassment,\" then she looked up and said, \"I
suppose we should get to your little demonstration then.\"

I said, \"Yes.\"

She thanked Kryz, Sharon and Brian once more, carefully shaking each of
their hands, and then she, Craig and I made our way in silence to the
conference room.

When we reached the conference room door, Eleanor stopped. \"I don\'t
need to see your demonstration. I want you to dismiss everyone and then
I will talk with just you and Gregor.\"

\"Dismiss?\" I said, worried by both her choice of words and her
instruction.

\"That\'s what I said.\" She looked at Craig. \"I\'m so sorry Craig, I
meant to thank you properly for all the good work you\'ve done for us,
but I need to talk to Steve and Gregor in private.

Craig tipped his head and said he understood. He shook both our hands
and left.

\"Eleanor,\" I said as I shook my head, indignant. \"This demonstration
is not just for your benefit. This team has worked hard on this and I
need you to acknowledge that and to say a few words of thanks.\"

\"Tough.\"

---

[[Full_Text/Chapter_36_Full|← Chapter 36 Full]] | [[Chapter 37 Full|📋 Summary]] | [[Full_Text/Chapter_38_Full|Chapter 38 Full →]]