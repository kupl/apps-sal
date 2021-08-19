def add_binary(a, b):

    def fun(x):
        return fun(x // 2) + str(x % 2) if x >= 1 else ''
    return fun(a + b)
