def combat(health, damage):
    x = health - damage
    return x if x > 0 else 0
