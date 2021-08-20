def combat(health, damage):
    f = health - damage
    return f if f > 0 else 0
