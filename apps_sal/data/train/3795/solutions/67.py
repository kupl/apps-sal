def combat(health, damage):
    after = health - damage
    if after < 0:
        return 0
    return after
