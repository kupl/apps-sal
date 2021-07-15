from collections import deque


class Bullet:

    def __init__(self, speed):
        self.speed = speed  # speed bullet travels
        self.location = 0  # distance travelled towards target

    def update(self):
        self.location += self.speed  # move bullet towards target


class Soldier:

    def __init__(self, number, firing_speed):
        self.number = number  # initial position of soldier in army
        self.firing_speed = firing_speed  # speed of bullets soldier fires


class Army:

    def __init__(self, number, firing_speeds):
        self.number = number  # number associated with army
        # convert input tuple of firing speeds of soldiers to deque of Soldier objects
        self.soldiers = deque()
        for n, firing_speed in enumerate(firing_speeds):
            self.soldiers.append(Soldier(n, firing_speed))


def queue_battle(distance, *args):
    """ Simulates battle. """

    armies = [Army(n, army) for n, army in enumerate(args)]  # list of Army objects

    while len(armies) > 1:  # while armies still fighting

        # reset bullets
        bullets = {army: [] for army in range(len(armies))}  # target: list of bullets moving towards target

        an_army_eliminated = False
        while not an_army_eliminated:  # fight until 1 or more armies eliminated

            # update bullet positions
            for army in range(len(armies)):
                for bullet in bullets[army]:
                    bullet.update()

            # for every army remove soldiers / fire as appropriate
            for army in range(len(armies)):

                for bullet in bullets[army]:
                    if bullet.location >= distance:  # remove leading soldier if hit by bullet before can fire
                        armies[army].soldiers.popleft()
                        if not armies[army].soldiers:  # mark an army has been eliminated
                            an_army_eliminated = True
                        break

                else:  # lead soldier not hit: fire and move to back
                    target = army + 1 if army + 1 < len(armies) else 0
                    firing_soldier = armies[army].soldiers[0]
                    bullets[target].append(Bullet(firing_soldier.firing_speed))  # fire
                    armies[army].soldiers.append(armies[army].soldiers.popleft())  # move to back

            # remove bullets that hit
            for army in range(len(armies)):
                bullets[army] = [bullet for bullet in bullets[army] if bullet.location < distance]

        armies = [army for army in armies if army.soldiers]  # eliminate armies with no soldiers remaining

    # return number of remaining army and numbers of remaining soldiers
    try:
        remaining_army = armies[0]
        return remaining_army.number, tuple(soldier.number for soldier in remaining_army.soldiers)
    except IndexError:  # no armies remain :(
        return -1, ()
