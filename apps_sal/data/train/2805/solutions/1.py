def productFib(prod):
    a,b = 0,1
    while a*b < prod:
        a,b = b, b+a
    return [a, b, a*b == prod]
