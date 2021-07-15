def is_divide_by(number, a, b):
    if ".0" not in str(number/a):
        return False
    if '.0' not in str(number/b):
        return False
    return True

