def combat(health, damage):
    result = health - damage
    if result < int(0):
        return result * 0
    else:
        return result
