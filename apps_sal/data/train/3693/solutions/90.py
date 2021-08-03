def make_negative(number):
    if number >= 1:
        number = number - number - number
        return number
    else:
        return number
