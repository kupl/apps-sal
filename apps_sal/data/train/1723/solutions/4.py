from abc import ABCMeta, abstractmethod


class Segment(metaclass=ABCMeta):

    @property
    @abstractmethod
    def control_points(self):
        pass

    @abstractmethod
    def point_at(self, t):
        pass

    @abstractmethod
    def sub_segment(self, t):
        pass


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

    def __rmul__(self, num):
        return Coordinate(self.x * num, self.y * num)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return "Coordinate(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def __hash__(self):
        return hash((self.x, self.y))


class Line(Segment):

    def __init__(self, *coords):
        self._control_points = coords
        self._P0 = Coordinate(coords[0], coords[1])
        self._P1 = Coordinate(coords[2], coords[3])

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        pt = (1 - t) * self._P0 + t * self._P1
        return pt.x, pt.y

    def sub_segment(self, t):
        return Line(self._P0.x, self._P0.y, *self.point_at(t))


class Quad(Segment):

    def __init__(self, *coords):
        self._control_points = coords
        self._P0 = Coordinate(coords[0], coords[1])
        self._P1 = Coordinate(coords[2], coords[3])
        self._P2 = Coordinate(coords[4], coords[5])

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        pt = (1 - t)**2 * self._P0 + 2 * (1 - t) * t * self._P1 + \
            t**2 * self._P2
        return pt.x, pt.y

    def sub_segment(self, t):
        sub_line = Line(self._P0.x, self._P0.y, self._P1.x, self._P1.y)
        return Quad(self._P0.x, self._P0.y, *sub_line.point_at(t),
                    *self.point_at(t))


class Cubic(Segment):

    def __init__(self, *coords):
        self._control_points = coords
        self._P0 = Coordinate(coords[0], coords[1])
        self._P1 = Coordinate(coords[2], coords[3])
        self._P2 = Coordinate(coords[4], coords[5])
        self._P3 = Coordinate(coords[6], coords[7])

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        pt = (1 - t)**3 * self._P0 + 3 * (1 - t)**2 * t * self._P1 + \
            3 * (1 - t) * t**2 * self._P2 + t**3 * self._P3
        return pt.x, pt.y

    def sub_segment(self, t):
        sub_line = Line(self._P0.x, self._P0.y, self._P1.x, self._P1.y)
        sub_quad = Quad(self._P0.x, self._P0.y, self._P1.x, self._P1.y,
                        self._P2.x, self._P2.y)
        return Cubic(self._P0.x, self._P0.y, *sub_line.point_at(t),
                     *sub_quad.point_at(t), *self.point_at(t))
