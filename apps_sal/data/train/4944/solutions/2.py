import numpy as np
class Vector:
    def __init__(self, *args):
        args = args[0] if len(args) == 1 else args
        self.x, self.y, self.z = args[0], args[1], args[2]
        self.li = [self.x,self.y,self.z]
        self.magnitude = np.linalg.norm(self.li)
    def __add__(self, other)   :   return Vector([i+j for i,j in zip(self.li,other.li)])
    def __sub__(self, other)   :   return Vector([i-j for i,j in zip(self.li,other.li)])
    def __eq__(self, other)    :   return all([i==j for i,j in zip(self.li,other.li)])
    def __str__(self)          :   return f'<{self.x}, {self.y}, {self.z}>'
    def cross(self, other)     :   return Vector(np.cross(self.li, other.li))
    def dot(self, other)       :   return np.dot(self.li,other.li)
    def to_tuple(self)         :   return tuple(self.li)
