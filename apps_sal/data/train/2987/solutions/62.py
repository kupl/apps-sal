def is_divide_by(number, a, b):
    x = 0
    if (number % a) == 0:
        x += 1
    if (number % b) == 0:
        x += 1
    if x == 2:
        return True
    else:
        return False
