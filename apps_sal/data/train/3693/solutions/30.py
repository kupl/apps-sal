def make_negative(number):
    # ...
    if number <= 0:
        return number
    else:
        number = (number * (-number)) / number
        return number
