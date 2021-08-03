def combat(health, damage):
    new_h = (health - damage)
    if new_h < 0:
        return 0
    else:
        return new_h
