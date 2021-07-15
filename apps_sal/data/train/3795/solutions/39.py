def combat(health, damage):
    res = health - damage
    return res if res > 0 else 0
