class Hero(object):
    (position, health, damage, experience, __init__) = ('00', 100, 5, 0, lambda self, name='Hero': setattr(self, 'name', name))
