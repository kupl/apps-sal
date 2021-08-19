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


class Line(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        (x0, y0, x1, y1) = self.control_points
        point = tuple(((1 - t) * p0 + t * p1 for (p0, p1) in [(x0, x1), (y0, y1)]))
        return point

    def sub_segment(self, t):
        return Line(*self.control_points[:2], *self.point_at(t))


class Quad(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        (x0, y0, x1, y1, x2, y2) = self.control_points
        point = tuple(((1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2 for (p0, p1, p2) in [(x0, x1, x2), (y0, y1, y2)]))
        return point

    def sub_segment(self, t):
        (x0, y0) = self.control_points[:2]
        (x1, y1) = Line(x0, y0, *self.control_points[2:4]).point_at(t)
        (x2, y2) = self.point_at(t)
        return Quad(x0, y0, x1, y1, x2, y2)


class Cubic(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        (x0, y0, x1, y1, x2, y2, x3, y3) = self.control_points
        point = tuple(((1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3 for (p0, p1, p2, p3) in [(x0, x1, x2, x3), (y0, y1, y2, y3)]))
        return point

    def sub_segment(self, t):
        (x0, y0) = self.control_points[:2]
        (x1, y1) = Line(x0, y0, *self.control_points[2:4]).point_at(t)
        (x2, y2) = Quad(*self.control_points[:6]).point_at(t)
        (x3, y3) = self.point_at(t)
        return Cubic(x0, y0, x1, y1, x2, y2, x3, y3)
