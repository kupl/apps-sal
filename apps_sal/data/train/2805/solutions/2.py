def productFib(prod):
    a, b = 0, 1
    rez = 0
    while rez < prod:
        a, b = b, a + b
        rez = a*b
    return [a, b, rez == prod]
