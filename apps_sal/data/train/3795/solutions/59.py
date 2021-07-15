def combat(health, damage):
    out = health - damage
    if out >= 0:
        return out
    else:
        return 0
