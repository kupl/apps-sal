def sharkovsky(a, b):
    while True:
        if a == 1 or b == 1:
            return a != 1
        if a % 2 or b % 2:
            return a % 2 == 1 and (not (b % 2 == 1 and a >= b))
        a /= 2
        b /= 2
