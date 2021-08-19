class Vector(object):

    def __init__(self, x, y):
        (self._x, self._y) = (x, y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def add(self, b):
        return Vector(self._x + b.x, self._y + b.y)
