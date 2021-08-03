def hero(bullets, dragons):
    alive = True
    if dragons * 2 > bullets:
        alive = False
    else:
        alive = True
    return alive
