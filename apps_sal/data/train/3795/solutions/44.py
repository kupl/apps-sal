def combat(health, damage):
    sub = health - damage
    return sub if sub > 0 else 0
