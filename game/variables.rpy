# Recurring Names
define bigdog = Character("Big Dog")
define mystery = Character("???")
# define narrator = Character(None, what_italic=True)

define you = Character("Sakura")

# Love interests

# Important Side Characters
define mom = Character("Mom")
define dad = Character("Dad")
define dad_stick = Character("Dad with a stick")
define sister = Character("Sister")

# Others
define bully1 = Character("Buff Jock")
define bully2 = Character("Somewhat Buff Jock")
define bully3 = Character("Luff Jock")
define cm1 = Character("Classmate 1")
define cm2 = Character("Classmate 2")

# Transitions
define bigdogintimidation = ComposeTransition(hpunch, after=zoomin)
define bigdogdissapearance = ComposeTransition(squares, before=blinds, after=irisin)