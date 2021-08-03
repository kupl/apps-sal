from operator import add, sub, mul, pow, truediv, mod


class value:
    def __init__(self, *v):
        self.v = v

    def compute(self): return self.f(self.v[0].v[0], self.v[1].v[0])


add, sub, mul, pow, truediv, mod = [type(f.__name__, (value,), {"f": f}) for f in [add, sub, mul, pow, truediv, mod]]
