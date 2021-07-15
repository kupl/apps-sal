class Hero(object):
    def __init__(self, name=None, experience=None, health= None, position= None, damage= None):
        self.name = name or 'Hero'
        self.experience = 0
        self.health = 100
        self.position = '00'
        self.damage = 5
