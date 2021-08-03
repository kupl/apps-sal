def is_divide_by(number, a, b):
    if (number % a == 0) & (number % b == 0):
        print(number % b)
        return True
    else:
        return False
