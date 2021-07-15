def cannons_ready(gunners):
    for k in gunners.values():
        if k == "nay":
            return "Shiver me timbers!"
    return "Fire!"
