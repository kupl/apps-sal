def combat(health, damage):
    health -= damage
    if health <= 0:
        return 0
    else:
        return health

