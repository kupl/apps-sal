def power_of_two(x):
    if x == 1:
        return True
    n = 2
    while n <= x:
        if x == n:
            return True
        n = n * 2
    return False
