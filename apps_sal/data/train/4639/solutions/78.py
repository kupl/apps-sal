def power_of_two(x):
    if x == 0:
        return False
    p = 1
    while p < x:
        p = p * 2
    if p == x:
        return True
    else:
        return False
