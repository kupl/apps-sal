def combat(health, damage):
    try:
        if health < damage:
            return 0
        else:
            return health - damage
    except:
        if health < 0:
            return 'health needs to be greater than zero'
