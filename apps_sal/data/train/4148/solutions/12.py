def sum_digits(number):
    if number < 0:
        number *= -1
    return sum(map(int, str(number)))
