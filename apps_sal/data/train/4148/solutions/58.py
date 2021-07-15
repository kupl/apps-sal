def sum_digits(number):
    abs_value = 0
    numbers = map(int, str(number).strip('-'))
    for i in numbers:
        abs_value += i
    return abs_value
