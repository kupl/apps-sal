def combat(health, damage):
    v=health-damage
    if v < 0:
        return 0
    else:
        return v
