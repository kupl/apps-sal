def combat(health, damage):
    if damage > health:
        return 0
    return health - damage
