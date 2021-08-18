def combat(health, damage):
    b = 0
    b = health - damage
    if b < 0:
        b = 0
    return b
