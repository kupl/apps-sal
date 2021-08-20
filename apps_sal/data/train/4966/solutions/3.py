class Fighter(object):

    def __init__(self, dict):
        self.name = dict['name']
        self.health = dict['health']
        self.speed = dict['speed']
        self.tact = dict['tactics']
        self.still_alive = True

    def battle(self, punch, point):
        self.health -= point.get(punch, 0)

    def raund(self, other, tact):
        if all((self.health > 0, self.tact)):
            punch = self.tact.pop(0)
            other.battle(punch, tact)
        else:
            self.still_alive = False


def fight(robot_1, robot_2, tactics):
    (f1, f2) = (Fighter(robot_1), Fighter(robot_2))
    fght = [sorted([f1, f2], key=lambda e: e.speed)[::-1], [f1, f2]][f1.speed == f2.speed]
    while fght[0].still_alive:
        fght[0].raund(fght[1], tactics)
        fght = fght[::-1]
    winer = [f1.name, f2.name][f2.health > f1.health]
    return [f'{winer} has won the fight.', 'The fight was a draw.'][f1.health == f2.health]
