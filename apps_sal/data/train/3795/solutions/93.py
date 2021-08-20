def combat(health, damage):
    return 0 if health - damage < 0 else health - damage
