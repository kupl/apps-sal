def make_negative(number):
    if number <= -1:
        return number
    elif number == 0:
        return 0
    else:
        return number - number * 2
