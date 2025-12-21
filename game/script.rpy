# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# moved to variables.rpy
# define e = Character("bigdog")
# define ee = Character("???")

# The game starts here.

label start:

    # hi carl... playing the music ! ! (placeholder)
    play music "vnshit.ogg"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg placeholder
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bigdog

    # These display lines of dialogue.

    e "i am the big dog who grants wishes"

    play music "panic.ogg"

    e "find my pages"
    e "find my pages"
    e "find my pages"
    e "find my pages"
    e "find my pages"

    call map_screen

    # Prologue
    call prologue

    # This ends the game.
    return
