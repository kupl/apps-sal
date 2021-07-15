from collections import deque

class Bullet:
    def __init__(self, speed, target_army):
        self.time_to_hit = DIST / speed
        self.target_army = target_army

    def increment_time(self, seconds):
        self.time_to_hit -= seconds

    def has_hit(self):
        return self.time_to_hit <= 0.0

class Soldier:
    def __init__(self, original_index, bullet_speed):
        self.original_index = original_index
        self.bullet_speed = bullet_speed


    def fire_bullet(self, target_army):
        return Bullet(self.bullet_speed, target_army)

class Army:
    def __init__(self, original_index, soldiers):
        # using deque for simpler rotations
        self.soldiers = deque(soldiers)
        self.original_index = original_index

    def fire_bullet(self, target_army):
        if self.is_wiped_out():
            raise Exception('tried to fire bullet on wiped out army!')

        bullet = self.soldiers[0].fire_bullet(target_army)
        self.soldiers.rotate(-1)
        return bullet


    def is_wiped_out(self):
        return len(self.soldiers) == 0

    def eliminate_head(self):
        if self.is_wiped_out():
            raise Exception('tried to kill someone on wiped out army!')
        self.soldiers.popleft()


class Battlefield:
    def __init__(self, armies):
        self.armies = armies
        self.bullets = []

    def increment_second(self):
        # need to keep track of which armies were already hit with a bullet, so we don't
        # eliminate more than one person per round
        armies_hit = []

        for bullet in self.bullets:
            bullet.increment_time(1)
            if bullet.has_hit() and bullet.target_army not in armies_hit:
                target = self.armies[bullet.target_army]
                target.eliminate_head()
                armies_hit.append(bullet.target_army)


        # each army which was not hit this round fires one bullet
        for i, army in enumerate(self.armies):
            if not i in armies_hit:
                bullet = army.fire_bullet((i + 1) % len(self.armies))
                self.bullets.append(bullet)

        
        if any(army.is_wiped_out() for army in self.armies):
            # reset bullet list
            self.bullets = []
            # reset army list(eliminate wiped out armies)
            self.armies = [army for army in self.armies if not army.is_wiped_out()]
        else:
            # remove bullets which have already reached their target
            self.bullets = [bullet for bullet in self.bullets if not bullet.has_hit()]


    def do_battle(self):
        while len(self.armies) > 1:
            self.increment_second()

        # return winner, or None
        return self.armies[0] if self.armies else None



def queue_battle(dist,*armies):
    # yes, I am too lazy to use these as constructor params for every class
    nonlocal DIST, N_ARMIES
    DIST = dist
    N_ARMIES = len(armies)
    
    army_list = []
    for i in range(N_ARMIES):
        soldiers = [Soldier(j, speed) for j, speed in enumerate(armies[i])]
        army_list.append(Army(i, soldiers))

    battlefield = Battlefield(army_list)
    winner = battlefield.do_battle()

    if winner is None:
        # no winner
        return -1,()
    else:
        soldiers = tuple([soldier.original_index for soldier in winner.soldiers])
        return winner.original_index, soldiers
