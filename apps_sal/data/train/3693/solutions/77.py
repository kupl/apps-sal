def make_negative(number):
    if number == 0:
        return number
    elif number < 0:
        return number
    else:
        number = -number
        return number


print(make_negative(1))
