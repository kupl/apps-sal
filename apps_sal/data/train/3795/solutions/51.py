def combat(health, damage):
    difference = health - damage
    if difference < 0:
        return 0
    else:
        return difference
