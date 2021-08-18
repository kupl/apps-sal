from collections import deque


class Bullet:

    def __init__(self, speed):
        self.speed = speed
        self.location = 0

    def update(self):
        self.location += self.speed


class Soldier:

    def __init__(self, number, firing_speed):
        self.number = number
        self.firing_speed = firing_speed


class Army:

    def __init__(self, number, firing_speeds):
        self.number = number
        self.soldiers = deque()
        for n, firing_speed in enumerate(firing_speeds):
            self.soldiers.append(Soldier(n, firing_speed))


def queue_battle(distance, *args):
    """ Simulates battle. """

    armies = [Army(n, army) for n, army in enumerate(args)]

    while len(armies) > 1:

        bullets = {army: [] for army in range(len(armies))}

        an_army_eliminated = False
        while not an_army_eliminated:

            for army in range(len(armies)):
                for bullet in bullets[army]:
                    bullet.update()

            for army in range(len(armies)):

                for bullet in bullets[army]:
                    if bullet.location >= distance:
                        armies[army].soldiers.popleft()
                        if not armies[army].soldiers:
                            an_army_eliminated = True
                        break

                else:
                    target = army + 1 if army + 1 < len(armies) else 0
                    firing_soldier = armies[army].soldiers[0]
                    bullets[target].append(Bullet(firing_soldier.firing_speed))
                    armies[army].soldiers.append(armies[army].soldiers.popleft())

            for army in range(len(armies)):
                bullets[army] = [bullet for bullet in bullets[army] if bullet.location < distance]

        armies = [army for army in armies if army.soldiers]

    try:
        remaining_army = armies[0]
        return remaining_army.number, tuple(soldier.number for soldier in remaining_army.soldiers)
    except IndexError:
        return -1, ()
