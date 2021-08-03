def make_negative(number):
    if number == 0:
        return 0
    elif number < 0:
        return number
    else:
        number = number * -1
        return number


make_negative(15)
