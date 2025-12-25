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
define bigdogintimidation = ComposeTransition(hpunch, after=zoomin)
define bigdogdissapearance = ComposeTransition(squares, before=blinds, after=irisin)

# Paths to take in the game 
default sister_lover = False 
# if this gets to like 5 we get the "big and fat" ending
default big_and_fat = 0