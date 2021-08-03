def is_divide_by(number, a, b):
    if(number % a == 0 and number % b == 0):
        return(True)
    else:
        return(False)


is_divide_by(-12, 2, -6)
is_divide_by(-12, 2, -5)
is_divide_by(45, 1, 6)
is_divide_by(45, 5, 15)
is_divide_by(4, 1, 4)
is_divide_by(15, -5, 3)
