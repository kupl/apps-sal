def combat(health, damage):
    all = health - damage

    if all > 0:
        return all
    else:
        return 0
