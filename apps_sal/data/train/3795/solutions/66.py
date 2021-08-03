def combat(health, damage):
    res = health - damage

    if res > 0:
        return res
    else:
        return 0
