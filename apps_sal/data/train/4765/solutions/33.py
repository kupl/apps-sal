class Hero(object):

    def __init__(self, *args):
        self.name = args[0] if args else 'Hero'
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
