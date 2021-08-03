def power_of_two(x):
    p = 1
    while p < x:
        p = p * 2
    return p == x
