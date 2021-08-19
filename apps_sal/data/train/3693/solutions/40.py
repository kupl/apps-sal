def make_negative(number):
    if number == 0:
        return number
    if '-' in str(number):
        return number
    return -number
