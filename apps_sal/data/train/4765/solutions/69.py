class Hero(object):
    def __init__(self, name=None):
        self.name = 'Hero' if not name else name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
