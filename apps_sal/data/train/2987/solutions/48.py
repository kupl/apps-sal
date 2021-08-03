def is_divide_by(number, a, b):
    x = (number / a)
    y = (number / b)
    if x.is_integer() == True and y.is_integer() == True:
        return True
    else:
        return False
