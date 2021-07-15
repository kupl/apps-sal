def combat(health, damage):
    list1 = health - damage
    if list1 > 0:
        return list1
    if list1 <= 0:
        return 0
