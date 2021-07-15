class Hero(object):
    def __init__(self, name='Hero', position='00', health=100, damage=5, experience=0):
        self.name = name
        self.experience = experience
        self.health = health
        self.position = position
        self.damage = damage
