def is_narcissistic(i):
    sum_of_digits = 0
    exponent = len(str(i))
    for digit in str(i):
        sum_of_digits += int(digit) ** exponent
    return sum_of_digits == i
