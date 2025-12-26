# Recurring Names
define bigdog = Character("Big Dog")
define mystery = Character("???")
# define narrator = Character(None, what_italic=True)

define you = Character("Sakura")

# Love interests
# All are placeholder names
define mainloveinterest = Character("Yuri")
define her_sister = Character("Yuri's Sister")
define puppy = Character("Smog")
define fourtran = Character("Ftran")

# Important Side Characters
define mom = Character("Mom")
define dad = Character("Dad")
define dad_stick = Character("Dad with a stick")
define sister = Character("Sister")

define teacher = Character("Teacher")
define nurse = Character("Big Tiddy Nurse")

# Others
define bully1 = Character("Buff Jock")
define bully2 = Character("Somewhat Buff Jock")
define bully3 = Character("Luff Jock")
define st1 = Character("Student 1")
define st2 = Character("Student 2")
define cm1 = Character("Classmate 1")
define cm2 = Character("Classmate 2")

# Transitions
define bigdogintimidation = ComposeTransition(hpunch, after=dissolve)
define bigdogdissapearance = ComposeTransition(squares, before=blinds, after=irisin)

# Romance paths

# Alterate Romance
default sister_lover = 0 
default nurse_lover = 0

# Alterate Paths to take in the game 
default big_and_fat = 0
default medically_inclined = 0
default healthy = 5 # if 6, then you've drank lukewarm water
default enlightened = 0

# Items 
default blackpill = 0

# Persistent Variables (newgame+, secret endings)
default persistent.knows_hiphop = False