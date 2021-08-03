def power_of_two(x):
    while x > 1 and x % 2 == 0:
        x = x // 2
    return x == 1
