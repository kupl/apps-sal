class Hero:
    """ Character: Hero. """

    def __init__(self, name: str = 'Hero', position: str = '00', health: int = 100, damage: int = 5, experience: int = 0):
        """ Prepare data. """
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience
