class F:

    def __init__(S, *a):
        S.a = a

    def compute(S):
        return __import__('operator').__dict__[type(S).__name__](*(x.compute() for x in S.a))


class value(F):

    def compute(S):
        return S.a[0]


class add(F):
    pass


class sub(F):
    pass


class mul(F):
    pass


class truediv(F):
    pass


class mod(F):
    pass


class pow(F):
    pass
