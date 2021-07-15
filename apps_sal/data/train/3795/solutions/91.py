def combat(health, damage):
    NewHealth = health - damage
    if NewHealth < 0:
        return 0
    else:
        return NewHealth
