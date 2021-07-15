from abc import ABCMeta, abstractmethod
from functools import reduce

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
    
def mul(a, b):
    return (a[0]*b , a[1]*b)
def add(*args):
    print(args)
    return (sum([args[i][0] + args[i + 1][0] for i in range(len(args) - 1)]),  sum([args[i][1] + args[i + 1][1] for i in range(len(args) - 1)]))  
class Line(Segment):

    def __init__(self, *c):
        self.c = c
        self.points = [(c[i], c[i+1]) for i in range(0, len(c) - 1, 2)]

    @property
    def control_points(self):
        return self.c

    def point_at(self, t):
        p = self.points
        return add(mul(p[0], 1 - t), mul(p[1], t)) 

    def sub_segment(self, t):
        return Line(self.c[0],self.c[1], self.point_at(t)[0], self.point_at(t)[1])


class Quad(Segment):

    def __init__(self, *c):
        self.c = c
        self.points = [(c[i], c[i+1]) for i in range(0, len(c) - 1, 2)]

    @property
    def control_points(self):
        return self.c

    def point_at(self, t):
        p = self.points
        return reduce(add, [mul(p[0], (1 - t)**2), mul(p[1], t*2*(1-t)), mul(p[2], t**2)])

    def sub_segment(self, t):
        a, b = add(mul(self.points[0], 1-t), mul(self.points[1], t))
        return Quad(self.c[0], self.c[1], a, b, self.point_at(t)[0], self.point_at(t)[1])

class Cubic(Segment):
    def __init__(self, *c):
        self.c = c
        self.points = [(c[i], c[i+1]) for i in range(0, len(c) - 1, 2)]

    @property
    def control_points(self):
        return self.c

    def point_at(self, t):
        p = self.points
        return reduce(add,[mul(p[0], (1 - t)**3), mul(p[1], 3*t*(1-t)**2), mul(p[2], 3*t**2*(1-t)), mul(p[3], t**3)])

    def sub_segment(self, t):
        p = self.points
        a, b =  add(mul(p[0], 1 - t), mul(p[1], t)) 
        c, d = reduce(add, [mul(p[0], (1 - t)**2), mul(p[1], t*2*(1-t)), mul(p[2], t**2)])
        return Cubic(self.c[0], self.c[1], a, b, c, d, self.point_at(t)[0], self.point_at(t)[1])
