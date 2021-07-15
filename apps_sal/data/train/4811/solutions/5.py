class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, other_vector):
        a = self.x + other_vector.x
        b = self.y + other_vector.y
        return Vector(a,b)

