class Vector:
    def __init__(s,*A):
        s.x,s.y,s.z=len(A)!=1 and A or A[0]
        s.magnitude=(s.x**2+s.y**2+s.z**2)**.5
    __str__=lambda s:"<%d, %d, %d>"%(s.x,s.y,s.z)
    __eq__=lambda s,o:(s.x,s.y,s.z)==(o.x,o.y,o.z)
    __add__=lambda s,o:Vector([s.x+o.x,s.y+o.y,s.z+o.z])
    __sub__=lambda s,o:Vector([s.x-o.x,s.y-o.y,s.z-o.z])
    to_tuple=lambda s:(s.x,s.y,s.z)
    dot=lambda s,o:s.x*o.x+s.y*o.y+s.z*o.z
    cross=lambda s,o:Vector(s.y*o.z-s.z*o.y,s.z*o.x-s.x*o.z,s.x*o.y-s.y*o.x)
