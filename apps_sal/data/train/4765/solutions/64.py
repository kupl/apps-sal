class Hero(object):
    def __init__(self,name=None):
        if name is None:
            name='Hero'
        self.name=name
        self.experience=0
        self.health=100
        self.position='00'
        self.damage=5

