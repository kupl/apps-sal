def combat(health, damage):
    after_hit = health - damage
    if after_hit >= 0:
        return after_hit
    else:
        return 0
