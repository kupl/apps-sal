def divide(weight):
    if (weight % 2 == 0) and (weight > 2):
        if (weight - 2) % 2 == 0:
            return True
        else:
            return False
    return False

