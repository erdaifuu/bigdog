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
    mom "Oh Sakura honey boo! Good morning my beautiful foid daughter!"
    "You watch mom kiss you on the forehead. She then leans you and squeeze both of your boobs with her hands."

    mom "Hasn't grown at much I see. Here's extra breakfast for you. A growing girl needs her food!"
    "She serves up a heaping plate of omurice and ramen."
    you "Am... I dreaming?"

    show dad default
    dad "Has anyone seen my stick? oh hello sakura my beautiful foid daughter :)"
    mom "Your sister still hasn't came downstairs, can you go wake her up?"
    hide dad default

    "I see a girl who looks slightly younger than I am walk downstairs, clearly excited to see me."
    sister "Ohayo onee-chan!"
    menu:        
        "Sister? I don't recall ever having a sister?":
            sister "Eeeeeehhhh?! Aw :c"
            you "Yeah... I think I'm going to head to school now."

        "SISTER?? HOLY WWWWWWW IMOUTOO!!!!":
            $ sister_lover = True 
            sister "Eeeeeehhhh?!"
            mom "Okay girl chill out. {w} I think you should leave for school now."

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
    st2 "Don't you know? That's Sakura, the Strongest Foid of Winfrey High!"

    window hide
    with vpunch 
    play audio school_bell 
    pause 
    "You hear the bell ring. It's time to go to class."

    # Scene changes to class
    teacher "Okay class. Now flip open your textbook to page 1!"
    
    cm1 "SAKURAAS HERE!!!"
    cm2 "OMG Sakura!"
    you "...I think I'm going to fricking barf. This is so uncomfy."
    you "Teach... I need to take a breather. I'm going to find the nurse with the fat boobs."

    "..."
    with hpunch
    mystery "Huff.. huff... sorry I'm late teacher-san! {w}Where... where's Sakura?"
    teacher "Girl sit tf down first! U always thinking bout sum Sakura."
    teacher "She just left for the nurse with the fat boobs. Hope she's feeling okay!"
    mystery "Oh... I guess I'll just have to catch her later then..."

    # Scene changes to nurse
    you ""

    return
