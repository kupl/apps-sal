class Vector:

    def __init__(self, a, b=None, c=None):
        if c is None:
            (a, b, c) = a
        self.x = a
        self.y = b
        self.z = c
        self.magnitude = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def __eq__(self, other):
        return self.to_tuple() == other.to_tuple()

    def cross(self, other):
        a = self.y * other.z - self.z * other.y
        b = self.z * other.x - self.x * other.z
        c = self.x * other.y - self.y * other.x
        return Vector(a, b, c)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return '<{}, {}, {}>'.format(*self.to_tuple())

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
