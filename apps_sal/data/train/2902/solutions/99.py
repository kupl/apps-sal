def opposite(number):
    if number < 0:
        return abs(number)
    if number > 0:
        return float('-' + str(number))
    if number == 0:
        return 0
