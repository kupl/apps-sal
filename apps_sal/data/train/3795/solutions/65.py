def combat(health, damage):
    k = health - damage
    if k<0:
        return 0
    return k
