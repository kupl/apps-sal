def divide(weight):
    half_weight = weight / 2
    if half_weight % 2 == 0:
        return True
    elif (half_weight - 1) % 2 == 0 and half_weight - 1 != 0:
        return True
    elif half_weight - 1 == 0:
        return False
    else:
        return False
