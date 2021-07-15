def cannons_ready(gunners):
    c=0
    for i in gunners:
        if gunners.get(i)=="nay":
            c=1
            break
    if c==1:
        return "Shiver me timbers!"
    else:
        return "Fire!"
