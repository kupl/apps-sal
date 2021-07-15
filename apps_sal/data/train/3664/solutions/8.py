def cat_mouse(x):
    place_of_cat = x.find("C")
    place_of_mouse = x.find("m")
    cat_towards_mouse = list(range(place_of_cat, place_of_cat + 5))
    mouse_towards_cat = list(range(place_of_mouse, place_of_mouse + 5))

    if place_of_mouse in cat_towards_mouse or place_of_cat in mouse_towards_cat:
        return "Caught!"
    else:
        return "Escaped!"
