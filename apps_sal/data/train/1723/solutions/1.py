class Segment:
    def __init__(self, *coords):
        self._control_points = list(zip(* [iter(coords)] * 2))

    def _flatten(self, points):
        return tuple(coord for point in points for coord in point)
    
    def _interpolate(self, points, t):
        return [tuple((1 - t) * x + t * y for x, y in zip(p0, p1))
                for p0, p1 in zip(points, points[1:])]
    
    def _reduce(self, points, t):
        while len(points) > 1:
            yield points[0]
            points = self._interpolate(points, t)
        yield points[0]

    @property
    def control_points(self):
        return self._flatten(self._control_points)

    def point_at(self, t):
        return list(self._reduce(self._control_points, t))[-1]

    def sub_segment(self, t):
        return self.__class__(*self._flatten(self._reduce(self._control_points, t)))

class Line(Segment): pass
class Quad(Segment): pass
class Cubic(Segment): pass
