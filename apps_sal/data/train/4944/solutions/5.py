from math import sqrt

class Vector:
    def __init__(self, *vector):
        self.vector = vector
        if len(vector) == 1:
           self.vector = tuple(vector[0])
        self.x, self.y, self.z = self.vector
        self.magnitude = sqrt(sum(v*v for v in self.vector))

    def to_tuple(self):
        return tuple(self.vector)

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def __add__(self, other):
        x, y, z = (a + other.vector[i] for i,a in enumerate(self.vector))
        return Vector(x, y, z)

    def __sub__(self, other):
        x, y, z = (a - other.vector[i] for i,a in enumerate(self.vector))
        return Vector(x, y, z)
    
    def __eq__(self, other):
        return all(v == other.vector[i] for i, v in enumerate(self.vector))

    def dot(self, other):
        return sum(v * other.vector[i] for i, v in enumerate(self.vector))

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = -(self.x * other.z - self.z * other.x)
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)
