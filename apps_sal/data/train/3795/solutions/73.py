def combat(health, damage):
    ret=health-damage
    if 0>ret:
        ret=0
    return ret
