def productFib(prod):

    def func(a, b):
        return func(b, a + b) if a * b < prod else [a, b, a * b == prod]
    return func(0, 1)
