def russian_peasant_multiplication(x, y):
    pro = 0
    while y != 0:
        if y % 2:
            pro += x
        x += x
        y //= 2
    return pro

