from operator import add, sub, mul, truediv

OPS = (("addition", add),
       ("subtraction", sub),
       ("multiplication", mul),
       ("division", truediv))


def calc_type(a, b, res):
    return next(kind for kind, f in OPS if f(a, b) == res)
