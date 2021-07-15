import numpy as np

class Vector:
    def __init__(self, *args):
        self.vec = np.array(args if type(args[0]) == int else args[0])
        self.x, self.y, self.z, self.magnitude = *self.vec, np.linalg.norm(self.vec)
    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'
    def __eq__(self, other):
        if type(other) != Vector: return False
        return np.array_equal(self.vec, other.vec)
    def __add__(self, other):
        return Vector(self.vec + other.vec)
    def __sub__(self, other):
        return Vector(self.vec - other.vec)
    def cross(self, other):
        return Vector(np.cross(self.vec, other.vec))
    def dot(self, other):
        return np.dot(self.vec, other.vec)
    def to_tuple(self):
        return tuple(self.vec)
