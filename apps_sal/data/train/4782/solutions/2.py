import operator


class Placeholder:
    def __init__(self, op=None, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

    def eval(self, args):
        if self.op:
            x, args = self.left.eval(args) if isinstance(self.left, Placeholder) else (self.left, args)
            y, args = self.right.eval(args) if isinstance(self.right, Placeholder) else (self.right, args)
            return self.op(x, y), args
        return args[0], args[1:]

    def __call__(self, *args):
        return self.eval(args)[0]

    def __add__(self, other):
        return Placeholder(op=operator.add, left=self, right=other)

    def __sub__(self, other):
        return Placeholder(op=operator.sub, left=self, right=other)

    def __mul__(self, other):
        return Placeholder(op=operator.mul, left=self, right=other)

    def __floordiv__(self, other):
        return Placeholder(op=operator.floordiv, left=self, right=other)

    def __radd__(self, other):
        return Placeholder(op=operator.add, left=other, right=self)

    def __rsub__(self, other):
        return Placeholder(op=operator.sub, left=other, right=self)

    def __rmul__(self, other):
        return Placeholder(op=operator.mul, left=other, right=self)

    def __rfloordiv__(self, other):
        return Placeholder(op=operator.floordiv, left=other, right=self)


x = Placeholder()
