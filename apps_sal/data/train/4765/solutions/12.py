class Hero(object):

    def __init__(self, name=None, position=None, health=None, damage=None, experience=None):
        self.name = name or 'Hero'
        self.position = position or '00'
        self.health = health or 100
        self.damage = damage or 5
        self.experience = experience or 0
