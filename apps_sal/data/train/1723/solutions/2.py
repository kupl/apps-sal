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
        x, y = self._control_points[::2], self._control_points[1::2]
        x0, y0, x1, y1 = self._control_points
        eq = lambda p, t: (1 - t) * p[0] + t * p[1]
        return eq(x, t), eq(y, t)

    def sub_segment(self, t):
        p0 = self._control_points[:2]
        pt = self.point_at(t)
        return self.__class__(*p0, *pt)


class Quad(Segment): 
    
    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        x, y = self._control_points[::2], self._control_points[1::2]
        eq = lambda p, t: (1 - t)**2 * p[0] + 2 * (1 - t) * t * p[1] + t**2 * p[2]
        return eq(x, t), eq(y, t)

    def sub_segment(self, t):
        p0 = self._control_points[:2]
        q0 = Line(*self._control_points[:4]).point_at(t)
        pt = self.point_at(t)
        return self.__class__(*p0, *q0, *pt)


class Cubic(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        x, y = self._control_points[::2], self._control_points[1::2]
        eq = lambda p, t: (1 - t)**3 * p[0] + 3 * (1 - t)**2 * t * p[1] + 3 * (1 - t) * t**2 * p[2] + t**3 * p[3]
        return eq(x, t), eq(y, t)

    def sub_segment(self, t):
        p0 = self._control_points[:2]
        q0 = Line(*self._control_points[:4]).point_at(t)
        q1 = Line(*self._control_points[2:6]).point_at(t)
        r0 = Line(*q0, *q1).point_at(t)
        pt = self.point_at(t)
        return self.__class__(*p0, *q0, *r0, *pt)
