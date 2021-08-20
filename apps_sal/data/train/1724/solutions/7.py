class Ship:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


def blast_sequence(aliens, position):
    result = []
    ships = [Ship(x, y, speed) for (x, row) in enumerate(aliens) for (y, speed) in enumerate(row) if speed]
    turn = 0
    while ships:
        for ship in ships:
            for _ in range(abs(ship.speed)):
                if ship.y == 0 and ship.speed < 0 or (ship.y == len(aliens[0]) - 1 and ship.speed > 0):
                    ship.x += 1
                    ship.speed *= -1
                    if ship.x == position[0]:
                        return None
                else:
                    ship.y += 1 if ship.speed > 0 else -1
        targets = [ship for ship in ships if ship.y == position[1]]
        targets.sort(key=lambda ship: (ship.x, abs(ship.speed), ship.speed))
        if targets:
            target = targets.pop()
            ships.remove(target)
            result.append(turn)
        turn += 1
    return result
