def divide(weight):
    if weight <= 0:
        return False
    return weight % 2 == 0 and weight > 2
