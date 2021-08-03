def combat(health, damage):
    if(health > damage):
        health = health - damage
        return health
    else:
        return 0
