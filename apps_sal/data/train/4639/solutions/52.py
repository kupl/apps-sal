def power_of_two(x):
    print(x)
    if x == 0:
        return False
    elif x == 1:
        return True
    while True:
        if x <= 0 or x == 1:
            return True
            break
        if x % 2 == 0:
            x = x // 2
        else:
            return False
