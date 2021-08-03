class Hero(object):
    def __init__(self, name=None):
        if name == None:
            self.name = 'Hero'
        else:
            self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
