label day1:
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

    cm1 "Wow that guy is such a fucking loser. Lol."
    cm2 "Girl ain't that right!"

    "I hold back tears and begin to walk home in the rain."
    
    # scene changes to the road / outside forest 
    # serene / mystical / rain music begins playing

    scene bg forest with fade
    "Without even thinking, I seem to have wandered into a forest."
    name "Huh, I don't recall there ever being a forest here."

    window hide
    play sound leavescrunching
    with hpunch
    pause
    play sound boom
    show bigdog neutral at left with bigdogintimidation
    pause
    
    name "N-nani desu ka?"
    bigdog "i am big dog. i have magic dayo. here i will prove my power."
    show bigdogmirror at right with dissolve
    bigdog "lol i just cloned myself"
    hide bigdogmirror with dissolve
    show bigdog happy
    bigdog "haha wasnt that cool"
    bigdog "anyway"
    show bigdog neutral with ease
    bigdog "Fate has brought u here young jit. I shall grant you the pleasure of one wish."

    menu wishes:
        "What do you wish for lil jit?"

        "I wish for a million wishes!":
            jump a_milli_ending

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



label a_milli_ending:
    bigdog "Nahh jit u greedy af"
    bigdog "Im boutta eat you!!!"
    name "AHHHHH!!!"
    hide bigdog neutral
    show bg black
    "You have perished. . ."
    call bigdogwisdom1
    $ renpy.full_restart()
    return