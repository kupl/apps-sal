class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
