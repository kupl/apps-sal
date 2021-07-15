def power_of_two(x):
    i = 1
    while i < x:
        i = i * 2
    if i == x:
        return True
    else:
        return False
