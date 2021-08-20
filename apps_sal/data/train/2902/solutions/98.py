def opposite(number):
    if number > 0:
        number = 0 - number
    elif number is None:
        number = -1
    else:
        return abs(number)
    return number
