def combat(health, damage):
    if damage > health:
        return 0
    elif health > damage:
        return health - damage
