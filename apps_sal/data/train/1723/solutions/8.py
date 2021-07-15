from abc import ABCMeta, abstractmethod
import numpy as np

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
        P0 = np.array(self._control_points[0:2])
        P1 = np.array(self._control_points[2:])
        return (1 - t) * P0 + t * P1


    def sub_segment(self, t):
        P0 = np.array(self._control_points[0:2])
        P1 = self.point_at(t)

        return Line(*P0,*P1)


class Quad(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        P0 = np.array(self._control_points[0:2])
        P1 = np.array(self._control_points[2:4])
        P2 = np.array(self._control_points[4:])
        return (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2

    def sub_segment(self, t):
        P0 = np.array(self._control_points[0:2])
        P1 = np.array(self._control_points[2:4])
        l1 = Line(*P0,*P1)
        P1_new = l1.point_at(t)
        P2 = np.array(self._control_points[4:])
        P2_new = self.point_at(t)

        return Quad(*P0,*P1_new,*P2_new)


class Cubic(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        P0 = np.array(self._control_points[0:2])
        P1 = np.array(self._control_points[2:4])
        P2 = np.array(self._control_points[4:6])
        P3 = np.array(self._control_points[6:])
        return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

    def sub_segment(self, t):
        P0 = np.array(self._control_points[0:2])
        P1 = np.array(self._control_points[2:4])
        P2 = np.array(self._control_points[4:6])
        P3 = np.array(self._control_points[6:])
        l1 = Line(*P0,*P1)
        P1_new = l1.point_at(t)
        l2 = Quad(*P0,*P1,*P2)
        P2_new = l2.point_at(t)
        P3_new = self.point_at(t)
        return Cubic(*P0,*P1_new,*P2_new,*P3_new)

