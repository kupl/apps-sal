class Hero(object):

    def __init__(self, name='Hero', experience=0, health=100, position='00', damage=5):
        self.name = name
        self.experience = experience
        self.health = health
        self.position = position
        self.damage = damage

    def name(self, name):
        return self.name

    def position(self):
        return self.position

    def health(self, health):
        return self.health

    def damage(self, damage):
        return self.damage
