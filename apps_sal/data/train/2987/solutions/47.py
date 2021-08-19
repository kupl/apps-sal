def is_divide_by(number, a, b):
    if int(number % a) == 0 and int(number % b) == 0:
        return True
    else:
        return False
