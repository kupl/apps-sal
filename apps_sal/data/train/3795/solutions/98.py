def combat(health, damage):
    print(health, damage)
    if damage > health:
        return 0
    else:
        health -= damage
        return health
