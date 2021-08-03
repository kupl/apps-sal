def is_divide_by(number, a, b):
    div1 = abs(number % a)
    print(div1)
    div2 = abs(number % b)
    print(div2)
    if (div1 == 0 and div2 == 0):
        return True
    else:
        return False
