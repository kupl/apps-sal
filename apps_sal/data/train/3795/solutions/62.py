def combat(health, damage):
    if health > damage:
        v = health - damage
        return (v)
    else:
        return (0)
