def combat(health, damage):
    result = health - damage
    if result < 0:
        result = 0
    return result
