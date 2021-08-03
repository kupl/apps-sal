def combat(health, damage):
    new = health - damage
    return new if new >= 0 else 0
