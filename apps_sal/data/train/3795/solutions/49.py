def combat(health, damage):
    ch=health-damage
    if ch>=0:
        return ch
    else:
        return 0
