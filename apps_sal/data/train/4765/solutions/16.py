class Hero(object):

    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = 'Hero'
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
