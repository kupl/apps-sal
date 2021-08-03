def is_divide_by(number, a, b):
    if number / a == int(number / a):
        if number / b == int(number / b):
            return True
        else:
            return False
    else:
        return False
