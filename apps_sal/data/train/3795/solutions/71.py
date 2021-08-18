def combat(health, damage):
    f = 0
    if health > damage:
        f = health - damage
    return f
