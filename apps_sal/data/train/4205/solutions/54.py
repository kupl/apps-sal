def cannons_ready(gunners):
    a = [v for v in gunners.values()]
    if "nay" in a:
        return "Shiver me timbers!"
    else:
        return "Fire!"
