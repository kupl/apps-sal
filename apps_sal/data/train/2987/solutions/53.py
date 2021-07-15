def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        divided = True
    else:
        divided = False
    return divided
