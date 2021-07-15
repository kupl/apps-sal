def combat(health, damage):
    t = health - damage
    return t if t >=0 else 0
