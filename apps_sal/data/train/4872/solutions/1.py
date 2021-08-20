import operator as op


class N:

    def __init__(s, *v):
        s.v = v

    def compute(s):
        return getattr(op, s.__class__.__name__)(s.v[0].c(), s.v[1].c())


class add(N):
    pass


class sub(N):
    pass


class mul(N):
    pass


class truediv(N):
    pass


class mod(N):
    pass


class pow(N):
    pass


class value(N):

    def c(s):
        return s.v[0]
