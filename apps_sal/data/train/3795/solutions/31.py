def combat(health, damage):
    if health - damage < 1:
        return 0
    else:
        return health - damage
