label day2:
    # Chicken does their good morning thing 
    
    scene bg bedroomafter with fade

    mystery "{i}Yawn...{/i} Good morning..."
    "I walked myself to the mirror. Ready to start another terrible day."

    # Scene changes to mirror
    mystery "Who...is this?"
    # Girl protagonist shows up in the mirror.
    mystery "That's... ME?!?!?!"

    # Scene change to downstairs
    "I race downstairs."
    scene bg kitchen
    show mom happy at left with dissolve
    mom "Oh Sakura honey boo! Good morning my beautiful foid daughter!"
    "You watch mom kiss you on the forehead. She then leans you and squeeze both of your boobs with her hands."

    mom "Hasn't grown at much I see. Here's extra breakfast for you. A growing girl needs her food!"
    "She serves up a heaping plate of omurice and ramen."
    you "Am... I dreaming?"

    show dad default at right with dissolve
    dad "Has anyone seen my stick? oh hello sakura my beautiful foid daughter :)"
    mom "Your sister still hasn't came downstairs, can you go wake her up?"
    hide dad default
    hide mom happy

    "I see a girl who looks slightly younger than I am walk downstairs, clearly excited to see me."
    show sister w with dissolve
    sister "Ohayo onee-chan!"
    menu:
        "Sister? I don't recall ever having a sister?":
            sister "Eeeeeehhhh?! You don't remember me desu? Aw :c"
            you "Yeah... I think I'm going to head to school now."

        "SISTER?? HOLY WWWWWWW IMOUTOO!!!!":
            $ sister_lover += 1
            sister "Eeeeeehhhh?! Onee-chan hentaiii!"
            mom "Okay girl chill tf out. {w}I think you should leave for school now."

        "{i}Epically ignores her and begins eating your omurice and ramen{/i}":
            $ big_and_fat += 1
            sister "Eeeeeehhhh?! Onee-chan is ignoring me?! :c"
            you "{i}Gulps up the rest of the food{/i} Oh man that was good. {w}Oh that is yummy. {w}Oh fuck that was so good. {w}I think I'm going to head to school now."
    
    show dad stick
    dad_stick "I found my stick. have a wonderful day at school !"
    hide dad stick with fade

    # Scene changes to school
    scene bg outsideschool
    "I speedily speed to school, trying to avoid anyone I know, but it seems that luck wasn't on my side."
    you "Oh shit, it's the jocks again."
    bully1 "is that... Sakura?"
    bully2 "Sakura-chan! It's so nice to see you!"
    bully1 "I heard you lost your umbrewwa yesterday. Here, I bought you a new one!"
    bully3 "Wanna join my crew"

    "I hurriedly pass them. This is creepy, do they have false memories about what happened before?"

    st1 "Wow she's such a stacy! Who's that?"
    st2 "Don't you know? That's Sakura, 「The Strongest Foid of Winfrey High」!"

    window hide
    with vpunch 
    play sound school_bell 
    pause 
    "You hear the bell ring. It's time to go to class."

    # Scene changes to class
    teacher "Okay class. Now flip open your textbook to page 1!"
    
    cm1 "SAKURAAS HERE!!!"
    cm2 "OMG Sakura!"
    you "...I think I'm going to fricking barf. This is so uncomfy."
    you "Teach... I need to take a breather. I'm going to find the nurse with the fat boobs."

    "..."
    with fade
    mystery "Huff.. huff... sorry I'm late teacher-san! {w}Where... where's Sakura?"
    teacher "Girl sit tf down first! U always thinking bout sum Sakura."
    teacher "She just left for the nurse with the fat boobs. Hope she's feeling okay!"
    mystery "Oh... I guess I'll just have to catch her later then..."
    with fade

    # Scene changes to nurse
    # She goes to the nurses office with stomach ache and the nurse has big fat boobies and then nurseshe leaves the the dog like squeezes through the door of the nurse offic

    nurse "Okay dear. You clearly look shaken up. Here's some lukewarm water to help with digestion and circulation."
    nurse "So what's wrong?"

    default told_the_truth = False 
    menu:
        "Tell her the truth.":
            $ told_the_truth = True
            $ enlightened += 1
            you "It's like I don't even know what is real anymore. My life is finally going the direction I've always wanted to go but it just feels so...{w=0.5} empty."
            nurse "I'm sorry but I'm just a school nurse. I really don't get paid enough for this. I'll be right back with some medicine."

        "Flirt with her.":
            $ nurse_lover += 1
            you "Nothing. Just wondering how you walk around with em things!"
            nurse "That's very sweet dear."
            you "Yeah lemme see em jiggle!"
            nurse "I think I'll be taking my leave now. I'll be back with some medicine."

        "Ask about the lukewarm water.":
            $ medically_inclined += 1
            you "What's with the... lukewarm water?"
            nurse "It helps with digestion and circulation."
            # nurse "If you want to learn more about this, come find me any time at my office."
            # $ nurse_unlocked = True
            nurse "In any case, I'll be taking my leave now. I'll be back with some medicine"
    
    play sound door_close fadeout 1.0
    if told_the_truth:
        you "That nurse was nice. I'm glad I got that off my chest. I {nw}wonder where she went."
    else:
        you "That nurse was nice. Still, it sucks.{w=0.5} I don't know if she's only nice to me because of my wish. All this feels so...{w=0.5} empty."
        you "Maybe I should have told her the truth. She seemed more dilligent at her job {nw}than I thought she would be."
    play sound boom
    play music bigdogtheme
    show bigdog neutral at left with bigdogintimidation
    bigdog "I heard you were having some internal doubts."
    bigdog "Do you regret your wish?"
    menu:
        "Yes. I don't want to live a lie.":
            pass
        "Maybe. I'm indecisive.":
            pass
        "No. Being a girl is kinda awesome.":
            pass
    bigdog "Well I don't gaf about your response actually. I can't be refunding every wish I give out just because there's regret. Gurl you is not at a Costco!"
    bigdog "But Big Dog is merciful. In a week, I'll come back and you can make this choice for real."
    show bigdog blush
    bigdog "But before that, you'll have to learn the {b}TRUE{/b} meaning of {b}LOVE{/b}!"
    show bigdog neutral
    bigdog "You can't really understand what your wish for \"people to like you\" means, if you don't even understand {b}LOVE{/b}."
    bigdog "And if you can't do that, then I'll just have to {nw}"
    show bigdog angry
    extend "{color=#f00}{b}FUCKING EAT YOU!!!!!!!!{/b}{/color}" with hpunch
    show bigdog blush
    bigdog "Or something like that. You'll understand in due time! Or should I say... jew time?"
    bigdog "Toodaloo!{w=0.15}{nw}"
    play sound byebye
    hide bigdog with bigdogdissapearance 
    pause
    you "Can you not do that?"

    "Time pass. All the things Big Dog said is still running through my head."
    "Deep in thought, I unknowingly fell asleep on the bed."
    
    # show night time outside school or smth, or dark nurse office
    with fade
    play sound school_end
    pause
    you "Yawnn... Oh fuck, class is over already. I need to run home."
    you "Before that, how is the nurse with the fat boobs still not back with my meds? Should I wait for her?"
    menu:
        "Go home right now":
            $ nurse_lover -= 1
            you "Fuck I can't do this. Today has been crazy for me. And I'm kinda hungry."
            you "Sorry nurse but I'm gone!"
        "Wait for the nurse":
            # $ nurse_lover += 1
            $ healthy += 1
            "..." 
            with fade
            nurse "I'm back. Take this, it might come in handy."
            # Plays success sound
            $ blackpill += 1
            "{i}「Black Pill」 get!{/i}"

    scene bg mchouse with fade
    return
