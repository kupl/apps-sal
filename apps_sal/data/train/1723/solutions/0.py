class Segment:  # Instead of an abstract class, make it the implementation for all three subclasses
    def __init__(self, *coords):
        self.control_points = coords  # IMHO a getter/setter is overkill here

    def control_points_at(self, t):  # Helper function
        p = self.control_points
        result = []
        while p:
            result.extend(p[:2])
            p = [v + (p[i+2] - v) * t for i, v in enumerate(p[:-2])]
        return result

    def point_at(self, t):
        return tuple(self.control_points_at(t)[-2:])

    def sub_segment(self, t):
        return self.__class__(*self.control_points_at(t))

class Line(Segment): pass
class Quad(Segment): pass
class Cubic(Segment): pass
