def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        ok = True
    else:
        ok = False
    return ok
