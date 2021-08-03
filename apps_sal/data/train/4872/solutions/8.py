class N:
    def __init__(s, a, b): s.a, s.b = a, b


class value(int):
    1


class add(N):
    def compute(s): return s.a + s.b


class sub(N):
    def compute(s): return s.a - s.b


class mul(N):
    def compute(s): return s.a * s.b


class truediv(N):
    def compute(s): return s.a / s.b


class mod(N):
    def compute(s): return s.a % s.b


class pow(N):
    def compute(s): return s.a**s.b
