def combat(health, damage):
    r = health - damage
    return r if r > 0 else 0
