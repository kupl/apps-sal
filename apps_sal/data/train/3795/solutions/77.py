def combat(health, damage):
    hit = health - damage
    if hit <= 0:
        return 0
    else:
        return hit
