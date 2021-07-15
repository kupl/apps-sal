def cannons_ready(gunners):
    return "Fire!" if all(s == "aye" for _, s in gunners.items()) else "Shiver me timbers!"
