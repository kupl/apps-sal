class Hero(object):
    def __init__(*args):
        self = args[0]
        if(len(args) == 2):
            self.name = args[1]
        else:
            self.name = "Hero"
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
myHero = Hero()

