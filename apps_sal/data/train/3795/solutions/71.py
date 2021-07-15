def combat(health, damage):
    #your code here
    f = 0
    if health > damage:
        f = health - damage
    return f
