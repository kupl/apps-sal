class Placeholder:

    def __init__(self, n, f):
        (self.n, self.f) = (n, f)

    def __call__(self, *args):
        return self.f(*args)

    def __add__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: self(*args[:self.n]) + other(*args[self.n:]))
        return Placeholder(self.n, lambda *args: self(*args) + other)

    def __sub__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: self(*args[:self.n]) - other(*args[self.n:]))
        return Placeholder(self.n, lambda *args: self(*args) - other)

    def __mul__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: self(*args[:self.n]) * other(*args[self.n:]))
        return Placeholder(self.n, lambda *args: self(*args) * other)

    def __floordiv__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: self(*args[:self.n]) // other(*args[self.n:]))
        return Placeholder(self.n, lambda *args: self(*args) // other)

    def __radd__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: other(*args[:self.n]) + self(*args[self.n:]))
        return Placeholder(self.n, lambda *args: other + self(*args))

    def __rsub__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: other(*args[:self.n]) - self(*args[self.n:]))
        return Placeholder(self.n, lambda *args: other - self(*args))

    def __rmul__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: other(*args[:self.n]) * self(*args[self.n:]))
        return Placeholder(self.n, lambda *args: other * self(*args))

    def __rfloordiv__(self, other):
        if isinstance(other, Placeholder):
            return Placeholder(self.n + other.n, lambda *args: other(*args[:self.n]) // self(*args[self.n:]))
        return Placeholder(self.n, lambda *args: other // self(*args))


x = Placeholder(1, int)
