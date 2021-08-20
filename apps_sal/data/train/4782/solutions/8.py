class Placeholder:

    def __init__(self, num=None):
        self.func = None
        self.needed = 1 if num is None else 0
        self.num = num
        self.left = None
        self.right = None

    def __call__(self, *args):
        if type(args[0]) == tuple:
            args = args[0]
        if self.func is None:
            return args[0] if self.num is None else self.num
        left = self.left(args[:self.left.needed])
        right = self.right(args[self.left.needed:])
        return self.func(left, right)

    def op(self, other, func):
        x = Placeholder()
        x.left = self
        x.right = Placeholder(other) if type(other) == int else other
        x.num = None
        x.func = func
        x.needed = x.left.needed + x.right.needed
        return x

    def __add__(self, other):
        return self.op(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.op(other, lambda x, y: x - y)

    def __mul__(self, other):
        return self.op(other, lambda x, y: x * y)

    def __floordiv__(self, other):
        return self.op(other, lambda x, y: x // y)

    def rop(self, other, func):
        x = Placeholder()
        x.right = self
        x.left = Placeholder(other) if type(other) == int else other
        x.num = None
        x.func = func
        x.needed = x.left.needed + x.right.needed
        return x

    def __radd__(self, other):
        return self.rop(other, lambda x, y: x + y)

    def __rsub__(self, other):
        return self.rop(other, lambda x, y: x - y)

    def __rmul__(self, other):
        return self.rop(other, lambda x, y: x * y)

    def __rfloordiv__(self, other):
        return self.rop(other, lambda x, y: x // y)


x = Placeholder()
