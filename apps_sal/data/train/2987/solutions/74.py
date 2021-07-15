def is_divide_by(number, a, b):
    result = number % a
    result2 = number % b
    if result == 0 and result2 == 0:
        return True
    return False

