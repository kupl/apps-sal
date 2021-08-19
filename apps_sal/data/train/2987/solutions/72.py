def is_divide_by(number, a, b):
    number = abs(number)
    a = abs(a)
    b = abs(b)
    return number % a == 0 and number % b == 0
