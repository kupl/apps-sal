def is_divide_by(number, a, b):
    flag = True
    if number % a == 0:
        if number % b == 0:
            flag = True
        else:
            flag = False
    else:
        flag = False
    return flag
