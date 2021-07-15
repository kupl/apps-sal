def combat(health, damage):
    if health < 0:
        return 0
    if health < damage:
        return 0
    return health - damage
