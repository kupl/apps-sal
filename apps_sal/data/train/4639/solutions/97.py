def power_of_two(x):
    n = 1
    while x > n:
        n *= 2
    return x == n
