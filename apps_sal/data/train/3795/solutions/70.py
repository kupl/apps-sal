def combat(health, damage):
    if damage < health:
        x=health-damage
    else:
        x=0
    return x
