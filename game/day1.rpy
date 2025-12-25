label day1:
    # scene: bedroom
   
    scene bg bedroombefore with fade
    "I wake up"

    # scene: kitchen

    scene bg kitchen with fade
    "I see scattered plates on the kitchen table. {w} Nary a scrap of food left though.
    {w} Once again my family has eaten without me . . ."
    "I grab a singular slice of bread and stumble out the door."

    # scene: street

    scene bg housestreet1 with fade
    "The street is quiet. {w} I start making my way towards the school. {w}
    Alone, as usual"

    # scene: outside the school

    scene bg outsideschool with fade
    "I keep my head down, avoiding eye contact as I enter the gate."
    "I speak to no one, {w} and no one speaks to me."

    # scene: inside the classroom

    scene bg classroom with fade
    "Classes are boring. {w} Time passes slowly."
    
    # scene: outside the school

    scene bg outsideschool with fade
    "It's raining..."
    "Guess I should go get my umbrella."

    bully1 "Yo loser! You looking for this?"
    "I watched the jock stomp on my dingy old umbrella until it's broken."

    $ name = renpy.input("What's your name?")
    $ name = name.strip() or "Satou"

    bully2 "Hahaha bro! You really showed [name] what he deserves!"
    bully1 "Hahaha thanks bro! High five!"
    bully3 "Heh, a loser like you will never have any nakamas! Now get out!" 

    st1 "Wow that guy is such a fucking loser. Lol."
    st2 "Girl ain't that right!"

    "I hold back tears and begin to walk home in the rain."
    
    # scene changes to the road / outside forest 
    # serene / mystical / rain music begins playing

    scene bg forest with fade
    play music forestsong
    "Without even thinking, I seem to have wandered into a forest."
    name "Huh, I don't recall there ever being a forest here."
    name "Well... I don't feel like going home just yet."
    "I find myself in a trance."
    "My legs move without any sort of effort on my part."
    "Minutes pass,{w} then tens of minutes,{w} until eventually"

    window hide
    play sound leavescrunching
    with hpunch
    pause
    play sound boom
    show bigdog neutral at left with bigdogintimidation
    pause
    
    play music bigdogtheme

    name "N-nani desu ka?"
    bigdog "i am big dog. i have magic dayo. here i will prove my power."
    show bigdogmirror at right with dissolve
    bigdog "lol i just cloned myself"
    hide bigdogmirror with dissolve
    show bigdog happy
    bigdog "haha wasnt that cool"
    bigdog "anyway"
    # remove this later 
    # like in day 10 or so we have some random scene that gives this so its newgame+
    $ persistent.knows_hiphop = True
    show bigdog neutral with ease
    bigdog "Fate has brought u here young jit. {w} I shall grant you the pleasure of one wish."

    menu wishes:
        "What do you wish for lil jit?"

        "I wish for a milli a milli a milli wishes" if persistent.knows_hiphop:
            jump a_milli_ending

        "I wish for a million wishes!":
            jump a_million_ending

        "I wish for people to like me!":
            bigdog "Hohoho... wish granted."

        "I wish for another wish!":
            bigdog "Okay. . . "
            jump wishes
    bigdog "In time you will learn .. ."
    bigdog "It's time to say goodbye now. Goodbye."
    window hide
    play sound byebye
    hide bigdog with bigdogdissapearance
    pause

    name "Okay. That just happened."

    # Scene changes to outside house
    scene bg mchouse with fade
    play music panic
    "When I finally get home, I was completely wet from head to toe. Because I didn't have my umbrella."

    # Scene changes to inside house
    scene bg kitchen with fade
    mom "Oh look who decided to come home completely wet from head to toe!"

    "I heard loud, unmistakable footsteps coming towards me. It's my dad with a stick."
    show dad stick
    dad_stick "I'm gonna hit you with my stick!"
    "He beats me viciously."
    hide dad stick
    mom "Annnd your dinner is going in the trash again. Jesus you're so fat. I'm putting you on a diet."
    "I watch her throw the heaping plate of spaghetti into the trash."
    "I run out of the room crying, as usual!"
    "Yep, that's my life."

    # Scene changes to your room 
    scene bg bedroombefore with fade
    # Scene changes to in front of your mirror, your figure shows inside
    name "That stupid big ass dog did nothing to me. I'm still miserable as per usual."
    name "Fuck my moidly features and my chud form."

    # Scene changes back to my room

    scene bg bedroombefore with fade

    # Sad music plays 
    "I cry myself to sleep."
    # Fade to black

    return 

label a_million_ending:
    play music bigdogevil
    show bigdog angry
    bigdog "Nahh jit u greedy af"
    show bigdog blush
    bigdog "Im boutta eat you!!!"
    name "AHHHHH!!!"
    hide bigdog neutral
    show bg black with fade
    "You have perished. . ."
    call bigdogwisdom1
    $ renpy.full_restart()
    return

# Secret newgame+ ending 
label a_milli_ending:
    show bigdog angry
    bigdog "Nahh jit u greedy af"
    show bigdog blush
    bigdog "But wait... nahhh you lowkey tapped in!!!{w} A millionaire I'm a young money millionaire"
    bigdog "Just this once... I might just allow you to do this"
    name "Yayyy thanks big dog!{w} But wym tapped in tho?"
    name "A Milli is like Lil Wayne's most popular song... like it's mainstream asf you making it sound like it's some underground grail"
    play music bigdogevil
    show bigdog angry with hpunch
    bigdog "Dude I've been stuck in this forest since the 12th century BCE"
    show bigdog neutral
    bigdog "Do you know how hard it is to be tapped into this shit when u stuck in a forest??? Lil Wayne IS the underground grail for me"
    name "My fault gang no disrespect like you got good taste and shit Lil Wayne is like one of the tops ykwim{w} even tho he's kinda fallen off lately"
    show bigdog angry
    bigdog "Fallen off? Fym???"
    name "Yeah like the Carter VI is fr hot ass. Also he was bitching when Kendrick got the superbowl instead of him like that's L behavior"
    bigdog "Nah I don't believe u, u fr just a hater hater"
    show bigdog neutral
    bigdog "Also Kendrick? Section 80 had like one good song, the one that went \"eight doobies to da face fuck dat\", everything else is hot garbage"
    name "Huh?? You didn't like Keisha's Song? Hol' Up? Rigamortis? Not even HiiiPower?{w} Also Kendrick way more versatile than that dawg like, you missing out if you haven't listened to GKMC or TPAB"
    show bigdog angry with hpunch
    bigdog "Shut the fuck up man!!! You don't know hiphop like I do!"
    name "Nah bro you just a pretentious old head! Open your ears bro! Like I bet ur the type to call the soundcloud wave all \"mumble rappers\" like get on with the times!"
    show bigdog angry with hpunch
    bigdog "I'm done with u man fr. I thought I met someone whos tapped in but u just a hater on god. I'm boutta EAT you"
    hide bigdog angry
    show bg black with fade
    "You have perished. . ."
    call bigdogwisdom100
    $ renpy.full_restart()
    # Secret ending locked