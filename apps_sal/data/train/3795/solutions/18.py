def combat(health, damage):
    #your code here
    if damage > health:
        return 0
    else:
        return abs(health - damage)
