class Hero(object):
    def __init__(self, *name):
        if name is ():
            self.name = 'Hero'
        else:
            self.name = name[0]
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
