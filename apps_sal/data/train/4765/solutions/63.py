class Hero(object):

    def __init__(self, name=None):
        self.name = 'Hero' if name is None else name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
