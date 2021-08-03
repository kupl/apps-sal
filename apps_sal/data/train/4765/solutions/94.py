class Hero(object):
    position = '00'
    health = 100
    damage = 5
    experience = 0

    def __init__(self, name=None):
        self.name = name if name else 'Hero'
