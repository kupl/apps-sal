class value:
    def __init__(self, v): self.v = v


class o:
    def __init__(self, a, b): A, B = a.v, b.v; self.r = {add: A + B, sub: A - B, mul: A * B, truediv: A / B, mod: A % B, pow: A**B}[type(self)]
    def compute(self): return self.r


class add(o):
    1


class sub(o):
    1


class mul(o):
    1


class truediv(o):
    1


class mod(o):
    1


class pow(o):
    1
