# a skeleton class with required operators provided for convenience
# feel free to use another approach
import operator


def placeholdify(other):
    if not isinstance(other, Placeholder):
        return Placeholder(lambda: other, 0)
    return other

def make_bin_op(op):
    def __op__(self, other):
        other = placeholdify(other)
        return Placeholder(
            lambda *args: op(self(*args[:self.n]), other(*args[self.n:])),
            self.n + other.n
        )
    return __op__
            
        
def make_bin_rop(op):
    def __rop__(self, other):
        other = placeholdify(other)
        return Placeholder(
            lambda *args: op(other(*args[:other.n]), self(*args[other.n:])),
            self.n + other.n
        )
    return __rop__


class Placeholder:
    def __init__(self, f, n):
        self.f = f
        self.n = n
    def __call__(self, *args):
        return self.f(*args)
    __add__ = make_bin_op(operator.add)
    __sub__ = make_bin_op(operator.sub)
    __mul__ = make_bin_op(operator.mul)
    __floordiv__ = make_bin_op(operator.floordiv)
    __radd__ = make_bin_rop(operator.add)
    __rsub__ = make_bin_rop(operator.sub)
    __rmul__ = make_bin_rop(operator.mul)
    __rfloordiv__ = make_bin_rop(operator.floordiv)

x = Placeholder(lambda x: x, 1)
