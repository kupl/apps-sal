class Hero(object):
    def __init__(self,*name):
        if name:self.name=name[0]
        else:self.name='Hero'
        self.position='00'
        self.health=100
        self.damage=5
        self.experience=0

