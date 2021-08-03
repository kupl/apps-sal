def make_negative(number):
    a = str(number)
    for i in a:
        if i in '-0':
            return number
    number = -1 * number
    return number
