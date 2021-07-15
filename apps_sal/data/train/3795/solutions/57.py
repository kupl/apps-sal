def combat(health, damage):
    r = health - damage
    if r < 0:
        return 0
    return r
