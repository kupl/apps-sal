class Hero(object):
    def __init__(self, name="Hero", position="00",
                 health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.max_health = health  # trust me, you want to have this as well
        self.health = health
        self.damage = damage
        self.experience = experience
