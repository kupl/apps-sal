def sum_digits(number):
    naked = str(number).strip('-')
    return sum(int(digit) for digit in naked)

