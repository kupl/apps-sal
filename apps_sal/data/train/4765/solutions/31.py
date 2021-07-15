class Hero(object):
    def __init__(self, *name):
        #Add default values here
        print(name)
        self.name = name[0] if name else 'Hero' 
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
