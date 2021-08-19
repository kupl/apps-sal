class Vector:

    def __init__(s, *A):
        (s.x, s.y, s.z) = len(A) != 1 and A or A[0]
        s.magnitude = (s.x ** 2 + s.y ** 2 + s.z ** 2) ** 0.5

    def __str__(s):
        return '<%d, %d, %d>' % (s.x, s.y, s.z)

    def __eq__(s, o):
        return (s.x, s.y, s.z) == (o.x, o.y, o.z)

    def __add__(s, o):
        return Vector([s.x + o.x, s.y + o.y, s.z + o.z])

    def __sub__(s, o):
        return Vector([s.x - o.x, s.y - o.y, s.z - o.z])

    def to_tuple(s):
        return (s.x, s.y, s.z)

    def dot(s, o):
        return s.x * o.x + s.y * o.y + s.z * o.z

    def cross(s, o):
        return Vector(s.y * o.z - s.z * o.y, s.z * o.x - s.x * o.z, s.x * o.y - s.y * o.x)
