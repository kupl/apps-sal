def productFib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)
