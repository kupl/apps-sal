class Hero(object):
    def __init__(self, name=("Hero")):  # Hero is default name
        self.name = name                # if name is given, than overwrite it
        self.experience = 0
        self.health = 100
        self.position = "00"
        self.damage = 5
