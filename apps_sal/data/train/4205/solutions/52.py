def cannons_ready(gunners):
    l = []
    for i in gunners:
        l.append(i)
    for i in l:
        if gunners.get(i) == "nay":
            return 'Shiver me timbers!'
    return "Fire!"
