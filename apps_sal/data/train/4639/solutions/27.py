def power_of_two(x):
    l = 1
    while l < x:
        l *= 2
    return l == x
