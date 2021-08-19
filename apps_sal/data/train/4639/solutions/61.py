def power_of_two(x):
    if x == 0:
        return False
    num = 1
    while num < x:
        num *= 2
    return num == x
