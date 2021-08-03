class Hero(object):
    def __init__(self, *name):
        if name:
            self.name = str(name)[2:-3]
        else:
            self.name = 'Hero'
        self.experience = 0
        self.health = 100
        self.position = '00'
        self.damage = 5
        pass
