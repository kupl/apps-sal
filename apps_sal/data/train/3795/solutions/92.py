def combat(health, damage):

    if health - damage <0:
       return 0
    elif health - damage > 0:
        return health - damage
    else:
        return int(health)
