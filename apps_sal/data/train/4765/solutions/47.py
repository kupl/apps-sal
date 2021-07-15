class Hero(object):
    def __init__(self, name=''):
        #Add default values here
        self.name = name or 'Hero'
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
