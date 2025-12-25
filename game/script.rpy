# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# moved to variables.rpy
# define e = Character("bigdog")
# define ee = Character("???")

# The game starts here.

label start:
    # hi carl... playing the music ! ! (placeholder)
    play music vnshit

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg placeholder
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show bigdog

    # These display lines of dialogue.

    # e "i am the big dog who grants wishes"

    # play music "panic.ogg"

    # e "find my pages"

    # Prologue
    # call prologue

    # e "where u gonna go?"
    # call map
    # $ dest = _return    

    # e "ohh u wanna go to da [dest]"
    # pause
    # "will {w} go {p} to da [dest]!"
    # call expression dest

    call day1 from _call_day1
    call day2 from _call_day2

    # This ends the game.
    return
