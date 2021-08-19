def power_of_two(x):
    # your code here
    if x == 0:
        return False
    elif (x / 2) % 2 == 0 and x % 2 == 0 and x % 4 == 0 and x % 8 == 0:
        return True
    else:
        if x == 1:
            return True
        else:
            return False
