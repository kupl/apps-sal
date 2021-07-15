class Hero(object):
    def __init__(self, name='Hero', experience=0, health=100, position='00', damage=5):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience
