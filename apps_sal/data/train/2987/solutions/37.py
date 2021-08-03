def is_divide_by(number, a, b):

    divide = number % a
    divide1 = number % b

    if divide != 0 or divide1 != 0:

        return False

    else:

        return True


is_divide_by(-12, 2, -6)
