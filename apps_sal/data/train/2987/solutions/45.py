def is_divide_by(number, a, b):
    print (type(number/a))
    if (number/a) % float(1) == 0 and (number/b) % float(1) == 0:
        return True
    else:
        return False
