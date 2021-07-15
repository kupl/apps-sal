def productFib(prod):
    for x, y in fib():
        if x * y == prod:
            return [x, y, True]
        elif x * y > prod:
            return [x, y, False]

def fib():
    a, b = 0, 1
    while True:
        yield a, b
        a, b = b, a + b
