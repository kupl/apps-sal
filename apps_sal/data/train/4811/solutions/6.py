class Vector(object):

    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def add(self, other):
        return self + other
