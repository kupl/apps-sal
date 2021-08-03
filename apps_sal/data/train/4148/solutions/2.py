def sum_digits(number):
    num_string = str(abs(number))
    total = 0

    for char in num_string:
        total += int(char)

    return total
