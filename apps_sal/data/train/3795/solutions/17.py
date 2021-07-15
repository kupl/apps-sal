def combat(health, damage):
    comb = health - damage
    if comb > 0:
        return comb
    else:
        return 0
