def combat(health, damage):
    if health - damage <= 0:
        return 0
    if health - damage > 0:
        return health - damage
