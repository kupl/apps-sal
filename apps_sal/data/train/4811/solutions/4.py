class Vector(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

