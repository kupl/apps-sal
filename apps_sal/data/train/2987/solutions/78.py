def is_divide_by(number, a, b):
    calc1 = number % a
    calc2 = number % b
    if calc1 == 0 and calc2 == 0:
        return True
    else:
        return False
