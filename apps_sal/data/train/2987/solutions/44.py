def is_divide_by(number, a, b):
    check = True
    c = number % a
    d = number % b
    if c or d != 0:
        check = False
    else:
        check = True
    return check
