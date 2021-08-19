def is_divide_by(number, a, b):
    c = number % a == 0
    d = number % b == 0
    return c and d
