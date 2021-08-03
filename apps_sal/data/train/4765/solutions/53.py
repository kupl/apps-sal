class Hero(object):
    name = 'Hero'
    experience = 0
    health = 100
    position = "00"
    damage = 5

    def __init__(self, name="Hero"):
        self.name = name
