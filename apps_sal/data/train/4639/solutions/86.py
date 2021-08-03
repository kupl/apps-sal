def power_of_two(x):
    for i in range(0, 128):
        if x == 2**i:
            return True
        elif x < 2**i:
            return False
