class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
