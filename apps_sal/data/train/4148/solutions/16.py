def sum_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total
