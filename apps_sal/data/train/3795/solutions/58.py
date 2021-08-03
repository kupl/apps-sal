def combat(health, damage):

    h = health
    d = damage
    x = h - d

    if x < 0:
        return 0
    else:
        return x
