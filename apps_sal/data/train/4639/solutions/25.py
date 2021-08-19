def power_of_two(x):
    start = 1
    while start < x:
        start *= 2
    return start == x
