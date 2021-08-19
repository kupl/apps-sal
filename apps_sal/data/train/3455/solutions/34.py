def disarium_number(number):
    x = sum([int(digit) ** (i + 1) for (i, digit) in enumerate(str(number))])
    if x == number:
        return 'Disarium !!'
    else:
        return 'Not !!'
