def is_divide_by(number, a, b):
    if number % a == 0:
        if number % b == 0:
            return True
        else:
            return False
    else:
        return False
