def power_of_two(x):
    num = 1
    while True:
        if x == num:
            return True
        elif x < num:
            return False
        num <<= 1
