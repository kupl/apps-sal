def is_divide_by(number, a, b):
    result = True
    if number % a == 0 and number % b == 0:
        result = True
    else:
        result = False
    return result
