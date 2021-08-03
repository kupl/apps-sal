class Hero(object):
    def __init__(self, name=None):
        self.name = name if name is not None else "Hero"
        self.experience = 0
        self.health = 100
        self.position = "00"
        self.damage = 5
