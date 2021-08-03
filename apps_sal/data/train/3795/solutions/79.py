def combat(health, damage):
    # your code here
    b = 0
    b = health - damage
    if b < 0:
        b = 0
    return b
