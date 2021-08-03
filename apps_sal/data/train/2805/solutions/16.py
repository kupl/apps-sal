def productFib(prod):
    if prod == 0:
        return [0, 1, True]
    a = 1
    b = 1
    for i in range(1, prod + 1):
        c = a + b
        if a * b == prod:
            return [a, b, True]
        elif a * b > prod:
            return [a, b, False]
        a = b
        b = c
