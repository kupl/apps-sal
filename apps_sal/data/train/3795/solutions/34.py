def combat(health, damage):
    hitpoints = health - damage
    if hitpoints < 0:
        return 0
    else:
        return hitpoints
