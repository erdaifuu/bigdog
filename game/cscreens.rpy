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
        action [Hide("map_screen"), Jump(location["scene"])]

  frame:
    xalign 1.0
    yalign 0.0
    textbutton "Return" xalign 0.5 yalign 0.5 action [Hide("map_screen")]

label map:
  $school_unlocked = True
  "Unlock school"

  show screen map_screen

  return

## Locations
label school:
  "You r at da school!"
  return
