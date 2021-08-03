from math import sqrt


class Vector:

    def __init__(self, *args):
        if isinstance(args[0], (list, tuple)):
            self.x, self.y, self.z = args[0]
        else:
            self.x, self.y, self.z = args

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __eq__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vector(other)
        return (
            self.magnitude == other.magnitude and
            self.x / other.x == self.y / other.y == self.z / other.z
        )

    def __str__(self):
        return "<%d, %d, %d>" % (self.x, self.y, self.z)

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def cross(self, other):
        return Vector(
            self.y * other.z - other.y * self.z,
            -(self.x * other.z - other.x * self.z),
            self.x * other.y - other.x * self.y
        )

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    @property
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
