class Vector(object):
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def add(self, v):
        x = v.x + self.x
        y = v.y + self.y
        return Vector(x,y)

