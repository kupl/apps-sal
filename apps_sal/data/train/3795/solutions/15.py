def combat(health, damage):
    owca = health - damage
    if owca < 0:
        return 0
    return owca
