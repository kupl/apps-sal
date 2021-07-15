import math
from collections import deque

class Alien:
    def __init__(self, health, trail_length):
        self.health = health
        self.trail_length = trail_length
        self.is_dummy = (health == 0)
        self.position = None

    def move(self):
        self.position += 1

    def place_on_board(self):
        self.position = 0

    def damage(self):
        self.health -= 1

    def on_map(self):
        return self.position < self.trail_length


class Turret:
    def __init__(self, loc, range, shots, name, trail):
        self.loc = loc
        self.range = range
        self.max_shots = shots
        self.name = name
        self.trail = trail
        self.current_shots = self.max_shots
        self.nothing_in_range = False
        self.in_range_list = deque()

        # Find all the spots in the trail, find which ones are in range
        for i, slot in enumerate(self.trail):
            if self.calc_dist(slot) <= self.range:
                self.in_range_list.appendleft(i)

    def reset_shots(self):
        self.nothing_in_range = False
        self.current_shots = self.max_shots

    def calc_dist(self, target):
        return math.sqrt(math.pow(target[0] - self.loc[0], 2) +
                         math.pow(target[1] - self.loc[1], 2))

    def shoot_nearest_alien(self, aliens):
        self.nothing_in_range = True

        if self.current_shots <= 0:
            return

        for slot in self.in_range_list:
            if slot < len(aliens):
                alien = aliens[slot]
                if alien.health > 0:
                    self.current_shots -= 1
                    alien.damage()
                    self.nothing_in_range = False
                    break


def gen_path(data):
    # Convert the raw string map to a mutable form so that we
    # can modify it later (to mark visited cells along the path)
    map = []
    for row in data:
        map.append(list(row))
    rows = len(map)
    cols = len(map[0])

    # Iterate through all the points and look for the unique
    # start of the trail (0) and while we're at it, find the
    # turrets (capital letters)
    start = None
    turrets = {}
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '0':
                start = (x, y)
            elif map[y][x].isupper():
                turrets[map[y][x]] = (x, y)

    # Now that we have the start, iterate through the map to
    # find the trail
    trail = []

    found_end = False
    next = start
    while not found_end:
        # South
        if next[1] + 1 < rows and map[next[1] + 1][next[0]] == "1":
            map[next[1] + 1][next[0]] = '0'  # mark as visited
            trail.append(next)
            next = (next[0], next[1] + 1)
        # North
        elif next[1] - 1 >= 0 and map[next[1] - 1][next[0]] == "1":
            map[next[1] - 1][next[0]] = '0'  # mark as visited
            trail.append(next)
            next = (next[0], next[1] - 1)
        # East
        elif next[0] + 1 < cols and map[next[1]][next[0] + 1] == "1":
            map[next[1]][next[0] + 1] = '0'  # mark as visited
            trail.append(next)
            next = (next[0] + 1, next[1])
        # West
        elif next[0] - 1 >= 0 and map[next[1]][next[0] - 1] == "1":
            map[next[1]][next[0] - 1] = '0'  # mark as visited
            trail.append(next)
            next = (next[0] - 1, next[1])
        else:
            trail.append(next)
            found_end = True
    return trail, turrets


def game_logic(turret_data, turret_locs, alien_data, trail):
    # Create an array of turret objects, combining the location information
    # and the range/shots information
    turrets = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter in turret_locs and letter in turret_data:
            turrets.append(Turret(turret_locs[letter],
                                  turret_data[letter][0],
                                  turret_data[letter][1],
                                  letter,
                                  trail))

    # Main loop variables
    aliens = deque()
    trail_length = len(trail)
    final_health = 0
    game_length = len(alien_data) + len(trail)
    round = 0

    # Perform the game logic here
    while round < game_length:  # This is the main tick loop of the game
        round += 1

        # Move the aliens
        if len(alien_data) > 0:
            aliens.appendleft(Alien(alien_data.pop(0), len(trail)))
        else:
            # Push dummies back after all the real aliens are used
            aliens.appendleft(Alien(0, len(trail)))

        # Check the right side of the list for aliens that fall off the map
        if len(aliens) > trail_length:
            removed_alien = aliens.pop()
            if removed_alien.health > 0:
                final_health += removed_alien.health

        # Reset all the turrets back to full power
        for turret in turrets:
            turret.reset_shots()

        # Iterate through all turrets
        turrets_done = False
        while not turrets_done:
            for t in turrets:
                if t.current_shots > 0:
                    t.shoot_nearest_alien(aliens)

            # Done condition: all turrets empty or
            # Have no enemies in range
            turrets_done = True
            for t in turrets:
                if t.current_shots > 0 and not t.nothing_in_range:
                    turrets_done = False
    return final_health

def tower_defense(grid,turrets,aliens):
    trail, turret_locs = gen_path(grid)
    total_health = game_logic(turrets, turret_locs, aliens, trail)
    return total_health
