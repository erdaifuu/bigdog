# Location selector
default school_unlocked = False

define locations = [
  # school 
  {
    "name": "school",
    "unlocked": "school_unlocked",
    "idle_image": "skool.png",
    "hover_image": "skool_hover.png",
    "scene": "school",
    "xalign": 0.4,
    "yalign": 0.55
  }
]

screen map_screen:
  modal True
  add "japan.png"

  for location in locations:
    $unlocked = eval(location["unlocked"])
    if unlocked:
      imagebutton:
        # button for unlocked 
        idle location["idle_image"]
        hover location["hover_image"]
        xalign location["xalign"]
        yalign location["yalign"]
        action [Hide("map_screen"), Return(location["scene"])]

  # remove later
  frame:
    xalign 1.0
    yalign 0.0
    textbutton "Return" xalign 0.5 yalign 0.5 action [Hide("map_screen")]

label map:
  # unlock the school
  $ school_unlocked = True

  # we choose a destination to go, doesn't actually call the destination here
  # $ means this is a single line of python code
  window hide
  $ dest = renpy.call_screen("map_screen")
  window show

  return dest

## Locations
label school:
  "You r at da school!"
  return "school"