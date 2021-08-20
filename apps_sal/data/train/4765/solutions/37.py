class Hero:

    def __init__(self, name='Hero', experience=0, health=100, position='00', damage=5):
        self.name = name
        self.experience = experience
        self.health = health
        self.position = position
        self.damage = damage

    def anzeige(self):
        return self.name
        return self.experience
        return self.health
        return self.position
        return self.damage
