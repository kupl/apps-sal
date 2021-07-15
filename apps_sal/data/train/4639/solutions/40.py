def power_of_two(x):
    start = 2
    while start < x:
        start *= 2
    return start == x or x == 1
