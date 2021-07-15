class Hero(object):
    position = '00'
    health = 100
    damage = 5
    experience = 0
    __init__ = lambda self, name='Hero': setattr(self, 'name', name)

