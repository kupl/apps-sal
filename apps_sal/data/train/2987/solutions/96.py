def is_divide_by(number, a, b):
    if number // a * a == number and number // b * b == number:
        return True
    return False
