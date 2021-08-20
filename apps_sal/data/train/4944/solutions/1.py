from operator import itemgetter, add, sub, mul
from itertools import starmap


class Vector(list):

    def __init__(self, *args):
        if len(args) == 1:
            args = args[0]
        super().__init__(args)
    (__add__, __sub__, __mul__) = (lambda self, o, f=fun: Vector(starmap(f, zip(self, o))) for fun in (add, sub, mul))
    (x, y, z) = (property(itemgetter(i)) for i in range(3))

    @property
    def magnitude(self):
        return self.dot(self) ** 0.5

    def __str__(self):
        return f"<{', '.join(map(str, self))}>"

    def to_tuple(self):
        return tuple(self)

    def dot(self, o):
        return sum(self * o)

    def cross(self, o):
        return Vector(self.y * o.z - self.z * o.y, self.z * o.x - self.x * o.z, self.x * o.y - self.y * o.x)
