def combat(health, damage):
    pv = health - damage
    return pv if pv > 0 else 0
