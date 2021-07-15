def cannons_ready(gunners):
    shoot = True
    for g in list(gunners.values()):
        if g == 'nay':
            shoot = False
    if shoot:
        return "Fire!"
    else:
        return "Shiver me timbers!"

