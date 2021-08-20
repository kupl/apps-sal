from math import factorial


class Coordinate(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __mul__(self, num):
        return Coordinate(self.x * num, self.y * num)
    __rmul__ = __mul__

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    __rsub__ = __sub__

    def __add__(self, other):
        try:
            return Coordinate(self.x + other.x, self.y + other.y)
        except AttributeError:
            return Coordinate(self.x + other, self.y + other)
    __radd__ = __add__

    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ', ' + str(self.y) + ')'

    def __str__(self):
        return 'C(' + str(self.x) + ', ' + str(self.y) + ')'

    def __hash__(self):
        return hash((self.x, self.y))


class Segment:

    def __init__(self, *coords):
        if len(coords) % 2 != 0:
            raise ValueError('Incorrect number of argument values.')
        self._control_points = coords
        self._P = [Coordinate(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]
        self._bezier_curve = self._get_bezier_curve(self._P)

    @property
    def control_points(self):
        return self._control_points

    @staticmethod
    def _comb(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    def _get_bezier_curve(self, points):
        n = len(points) - 1
        return lambda t: sum((self._comb(n, i) * t ** i * (1 - t) ** (n - i) * points[i] for i in range(n + 1)))

    def point_at(self, t):
        pt = self._bezier_curve(t)
        return (pt.x, pt.y)

    def sub_segment(self, t):
        sub_points = [*self._control_points[:2]]
        for i in range(4, len(self._control_points), 2):
            point = Segment(*self._control_points[:i]).point_at(t)
            sub_points.extend(point)
        sub_points.extend(self.point_at(t))
        return Segment(*sub_points)


class Line(Segment):
    pass


class Quad(Segment):
    pass


class Cubic(Segment):
    pass
