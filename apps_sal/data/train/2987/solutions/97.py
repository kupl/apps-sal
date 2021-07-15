def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        is_divide_by = True
    else:
        is_divide_by = False
    return is_divide_by
