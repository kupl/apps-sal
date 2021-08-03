def cannons_ready(gunners):
    print(gunners)
    for i in gunners:
        if gunners[i] == "nay":
            return 'Shiver me timbers!'
            break
    else:
        return "Fire!"
