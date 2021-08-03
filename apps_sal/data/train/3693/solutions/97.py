def make_negative(number):
    if number < 0:
        return number
    else:
        number -= 2 * number
        return number
