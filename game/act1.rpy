label day1:
    # scene: outside the school
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
    "Without even thinking, I seem to have wandered into a forest."
    name "Huh, I don't recall there ever being a forest here."

    window hide
    play sound leavescrunching
    with hpunch
    pause
    play sound boom
    show bigdog with bigdogintimidation
    pause
    window show
    
    name "N-nani desu ka?"
    bigdog "Fate has brought u here young jit. I shall grant you the pleasure of one wish."

    menu wishes:
        "What do you wish for lil jit?"

        "I wish for a million wishes!":
            jump a_milli_ending

        "I wish for people to like me!":
            bigdog "Hohoho... wish granted."

        "I wish for another wish!":
            jump wishes
    
    bigdog "It's time to say goodbye now. Goodbye."
    hide bigdog with bigdogdissapearance
    pause

    name "I really need to sniff less glue."

    # Scene changes to outside house
    "When I finally get home, I was completely wet from head to toe. Because I didn't have my umbrella."

    # Scene changes to inside house
    mom "Oh look who decided to come home completely wet from head to toe!"

    "I heard loud, unmistakable footsteps coming towards me. It's my dad with a stick."
    show dad_stick
    dad_stick "I'm gonna hit you with my stick!"
    "He beats me viciously."
    hide dad_stick
    mom "Annnd your dinner is going in the trash again. Jesus you're so fat. I'm putting you on a diet."
    "I watch her throw the heaping plate of spaghetti into the trash."
    "I run out of the room crying, as usual!"
    "Yep, that's my life."

    # Scene changes to your room 
    # Scene changes to in front of your mirror, your figure shows inside
    name "I should have known that stupid big ass dog wasn't real."
    name "I'm still miserable as per usual. Not to mention my moidly features and my chud form."

    # Scene changes back to my room
    # Sad music plays 
    "I cry myself to sleep."
    # Fade to black

    return 

label day2:
    # Chicken does their good morning thing 
    scene bg placeholder
    with fade

    mystery "{i}Yawn...{/i} Good morning..."
    "I walked myself to the mirror. Ready to start another terrible day."

    # Scene changes to mirror
    mystery "Who...is this?"
    # Girl protagonist shows up in the mirror.
    mystery "That's... ME?!?!?!"

    # Scene change to downstairs
    "I race downstairs."

    mom "Oh Sakura honey boo! Good morning my beautiful foid daughter!"
    "You watch mom kiss you on the forehead. She then leans you and squeeze both of your boobs with her hands."

    mom "Hasn't grown at much I see. Here's extra breakfast for you. A growing girl needs her food!"
    "She serves up a heaping plate of omurice and ramen."
    you "Am... I dreaming?"

    show dad
    dad "Has anyone seen my stick? oh hello sakura my beautiful foid daughter :)"
    mom "Your sister still hasn't came downstairs, can you go wake her up?"
    hide dad

    you "Okay now it's kinda creepy. Sister?? I don't recall ever having a sister?"
    "I see a girl who looks slightly younger than I am walk downstairs, clearly excited to see me."
    sister "Ohayo onee-chan!"
    you "Yeah... I think I'm going to head to school now."
    
    show dad_stick
    dad_stick "I found my stick. have a wonderful day at school !"
    hide dad_stick with fade

    # Scene changes to school

    return

label a_milli_ending:
    bigdog "Nahh jit u greedy af"
    bigdog "Im boutta eat you!!!"
    name "AHHHHH!!!"
    $ renpy.full_restart()
    return