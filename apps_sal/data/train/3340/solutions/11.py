def sharkovsky(a, b):
    if a % 2 == 0 and b % 2 == 0:
        while a % 2 == 0 and b % 2 == 0:
            a = a / 2
            b = b / 2

    if b % 2 == 0:
        if a == 1:
            return 1 == 2
        else:
            return 1 == 1
    elif a % 2 == 0:
        if b == 1:
            return 1 == 1
        else:
            return 1 == 2
    else:
        if b == 1:
            return 1 == 1
        elif a == 1:
            return 1 == 2
        else:
            return a < b
