def sum_digits(number):
    for i in str(number):
        if i == '-':
            number = str(number).strip('-')
        else:
            pass
        digits = [int(x) for x in str(number)]
    return sum(digits)
