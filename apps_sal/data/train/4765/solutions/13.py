class Hero(object):

    def __init__(self, *name):
        self.name = 'Hero'
        for a in name:
            self.name = name[0]
        self.experience = 0
        self.position = '00'
        self.health = 100
        self.damage = 5
