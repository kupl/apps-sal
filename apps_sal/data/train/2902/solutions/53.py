def opposite(number):
    x = '-' + str(number)
    if number < 0:
        return abs(number)
    else:
        return float(x)
