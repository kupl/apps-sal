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
        p_0, p_1, p_2, p_3 = self.control_points[0], self.control_points[1], self.control_points[2], self.control_points[3]
        x = (1 - t) * p_0 + t * p_2
        y = (1 - t) * p_1 + t * p_3
        return (x, y)

    def sub_segment(self, t):
        t_point = self.point_at(t)
        co_ords = (self.control_points[0], self.control_points[1], t_point[0], t_point[1])
        return Line(*co_ords)


class Quad(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        p_1 = (self.control_points[0], self.control_points[1])
        p_2 = (self.control_points[2], self.control_points[3])
        p_3 = (self.control_points[4], self.control_points[5])
        x = (1 - t)**2 * p_1[0] + 2 * (1 - t) * t * p_2[0] + t**2 * p_3[0]
        y = (1 - t)**2 * p_1[1] + 2 * (1 - t) * t * p_2[1] + t**2 * p_3[1]
        return (x, y)

    def sub_segment(self, t):
        lne = Line(self.control_points[0], self.control_points[1], self.control_points[2], self.control_points[3])
        t_p1 = lne.point_at(t)
        t_point = self.point_at(t)
        co_ords = (self.control_points[0], self.control_points[1], t_p1[0], t_p1[1], t_point[0], t_point[1])
        return Quad(*co_ords)


class Cubic(Segment):

    def __init__(self, *coords):
        self._control_points = coords

    @property
    def control_points(self):
        return self._control_points

    def point_at(self, t):
        p_1 = (self.control_points[0], self.control_points[1])
        p_2 = (self.control_points[2], self.control_points[3])
        p_3 = (self.control_points[4], self.control_points[5])
        p_4 = (self.control_points[6], self.control_points[7])
        x = (1 - t)**3 * p_1[0] + 3 * (1 - t)**2 * t * p_2[0] + 3 * (1 - t) * t**2 * p_3[0] + t**3 * p_4[0]
        y = (1 - t)**3 * p_1[1] + 3 * (1 - t)**2 * t * p_2[1] + 3 * (1 - t) * t**2 * p_3[1] + t**3 * p_4[1]
        return (x, y)

    def sub_segment(self, t):
        t_point = self.point_at(t)
        lne_1 = Line(self.control_points[0], self.control_points[1], self.control_points[2], self.control_points[3])
        pnt_1 = lne_1.point_at(t)
        lne_2 = Line(self.control_points[2], self.control_points[3], self.control_points[4], self.control_points[5])
        pnt_2 = lne_2.point_at(t)
        lne_3 = Line(self.control_points[4], self.control_points[5], self.control_points[6], self.control_points[7])
        pnt_3 = lne_3.point_at(t)
        lne_g1 = Line(*pnt_1, *pnt_2)
        pnt_g1 = lne_g1.point_at(t)
        lne_g2 = Line(*pnt_2, *pnt_3)
        co_ords = (self.control_points[0], self.control_points[1], pnt_1[0], pnt_1[1], pnt_g1[0], pnt_g1[1], t_point[0], t_point[1])
        return Cubic(*co_ords)
