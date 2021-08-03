def divide(weight):
    if weight % 2 == 0:
        for i in range(1, weight):
            remainder = weight - i
            if remainder % 2 == 0 and i % 2 == 0:
                return True
        return False
    else:
        return False
