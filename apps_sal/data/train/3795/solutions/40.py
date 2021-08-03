def combat(health, damage):
    if health < damage:
        return 0
    else:
        return abs(health - damage)
