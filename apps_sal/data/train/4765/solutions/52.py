class Hero(object):

    def __init__(self, name=''):
        self.name = name if name else 'Hero'
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
