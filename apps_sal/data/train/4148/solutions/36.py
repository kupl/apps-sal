def sum_digits(number):
    if number < 0:
        number *= -1
    a = str(number)
    return sum([int(i) for i in a])
