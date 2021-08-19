from collections import deque
log = False


class Game():

    def __init__(self, distance, armies):
        self.round = 0
        self.victory = False
        self.distance = distance
        self.armies = deque([Army(position=i, members=army_tuple) for i, army_tuple in enumerate(armies)])
        self.bullets = set()

    def print_state(self):
        if log:
            print('Armies:')
            for army in self.armies:
                print(army)
            if self.bullets:
                print('Bullets:')
                for bullet in self.bullets:
                    print(bullet)

    def assign_targets(self):
        if log:
            print('-> Assigning targets')
        for army, target in zip(self.armies, range(1, len(self.armies) + 1)):
            if target == len(self.armies):
                target = 0
            army.target = self.armies[target]
        self.print_state()

    def move_bullets(self):
        if log:
            print('-> Moving bullets')
        for bullet in self.bullets:
            bullet.move()
        self.print_state()

    def kill_leaders(self):
        if log:
            print('-> Killing army leaders')
        for bullet in self.bullets:
            if bullet.distance_to_target <= 0:
                bullet.target.leader.alive = False
        self.bullets = {b for b in self.bullets if b.distance_to_target > 0}  # Clear bullets
        self.print_state()

    def fire_bullets(self):
        if log:
            print('-> Firing bullets')
        for army in self.armies:
            if army.leader.alive:
                self.bullets.add(Bullet(target=army.target, speed=army.leader.bullet_speed, distance_to_target=self.distance))
        self.print_state()

    def regroup_armies(self):
        if log:
            print('-> Regrouping armies')
        for army in self.armies:
            army.regroup()
        original_armies_count = len(self.armies)
        self.armies = deque([army for army in self.armies if len(army.soldiers) > 0])
        if len(self.armies) < original_armies_count:
            self.bullets = set()
        if len(self.armies) <= 1:
            self.victory = True
        self.print_state()

    def render_victory(self):
        if len(self.armies) < 1:
            return (-1, ())
        else:
            return (self.armies[0].original_position, tuple([s.original_position for s in self.armies[0].soldiers]))

    def game_loop(self):
        while True:
            if log:
                print('--> Executing round {}'.format(self.round))
            self.print_state()
            self.assign_targets()
            self.move_bullets()
            self.kill_leaders()
            self.fire_bullets()
            self.regroup_armies()
            if self.victory:
                break
            self.round += 1


class Army():

    def __init__(self, position, members):
        self.original_position = position
        self.soldiers = deque([Soldier(position=i, bullet_speed=bs) for i, bs in enumerate(members)])
        self.leader = self.soldiers[0]
        self.target = None

    def regroup(self):
        if self.leader.alive:
            self.soldiers.append(self.soldiers.popleft())  # Move head to the back
        else:
            self.soldiers.popleft()  # Head just dies
        if len(self.soldiers) > 0:
            self.leader = self.soldiers[0]
        else:
            self.leader = None

    def __str__(self):
        return 'Army {army_number} [Soldires: {soldiers}, Leader: {leader}, Target: {target}]'.format(
            army_number=self.original_position,
            soldiers=self.soldiers,
            leader=self.leader,
            target=repr(self.target)
        )

    def __repr__(self):
        return 'Army {}'.format(self.original_position)


class Soldier():

    def __init__(self, position, bullet_speed):
        self.original_position = position
        self.bullet_speed = bullet_speed
        self.alive = True

    def __repr__(self):
        return '({bullet_speed}, {alive_status})'.format(
            bullet_speed=self.bullet_speed,
            alive_status='alive' if self.alive else 'dead'
        )


class Bullet():

    def __init__(self, target, speed, distance_to_target):
        self.target = target
        self.speed = speed
        self.distance_to_target = distance_to_target

    def __str__(self):
        return 'Bullet [Target: {target}, Dist: {distance}, Speed: {speed}]'.format(
            target=repr(self.target),
            distance=self.distance_to_target,
            speed=self.speed
        )

    def move(self):
        self.distance_to_target -= self.speed


def queue_battle(dist, *armies):
    game = Game(dist, armies)
    game.game_loop()

    return game.render_victory()
