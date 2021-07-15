def combat(health, damage):
    while health - damage > 0:
        return health - damage
    else:
        return 0
