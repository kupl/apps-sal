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
        self.cp = coords
        self.P0 = (coords[0], coords[1])
        self.P1 = (coords[2], coords[3])

    @property
    def control_points(self):
        return self.cp

    def point_at(self, t):
        x = (1 - t) * self.P0[0] + t * self.P1[0]
        y = (1 - t) * self.P0[1] + t * self.P1[1]
        return (x, y)

    def sub_segment(self, t):
        return Line(*self.P0, *self.point_at(t))


class Quad(Segment):

    def __init__(self, *coords):
        self.cp = coords
        self.P = [(coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5])]

    @property
    def control_points(self):
        return self.cp

    def get_Q(self, t):
        return (Line(*self.P[0], *self.P[1]).point_at(t), Line(*self.P[1], *self.P[2]).point_at(t))

    def point_at(self, t):
        Q = self.get_Q(t)
        return Line(*Q[0], *Q[1]).point_at(t)

    def sub_segment(self, t):
        Q = self.get_Q(t)[0]
        B = self.point_at(t)
        return Quad(*self.P[0], *Q, *B)


class Cubic(Segment):

    def __init__(self, *coords):
        self.cp = coords
        self.P = [(coords[0], coords[1]), (coords[2], coords[3]), (coords[4], coords[5]), (coords[6], coords[7])]

    @property
    def control_points(self):
        return self.cp

    def get_Q(self, t):
        return (Line(*self.P[0], *self.P[1]).point_at(t), Line(*self.P[1], *self.P[2]).point_at(t), Line(*self.P[2], *self.P[3]).point_at(t))

    def point_at(self, t):
        Q = self.get_Q(t)
        return Quad(*Q[0], *Q[1], *Q[2]).point_at(t)

    def sub_segment(self, t):
        Q = self.get_Q(t)
        R = Line(*Q[0], *Q[1]).point_at(t)
        B = self.point_at(t)
        return Cubic(*self.P[0], *Q[0], *R, *B)
