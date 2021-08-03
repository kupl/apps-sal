def divide(weight):
    a = 1
    if weight % 2 == 0 and weight > 2:
        while a < weight:
            b = weight - a
            if a % 2 == 0 and b % 2 == 0:
                return True
            a += 1
    else:
        return False
