def divide(weight):
    for x in range(1, weight):
        if x%2 == 0 and (weight-x)%2 == 0:
            return True
    else:
        return False
