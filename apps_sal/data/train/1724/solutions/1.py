class Ship:
    columns = 0

    def __init__(self, row, col, speed):
        self.row = row
        self.col = col
        self.speed = speed

    def move(self):
        new_col = self.col + self.speed
        if new_col < 0 or new_col >= Ship.columns:
            self.row += 1
            self.speed = -self.speed
            if new_col < 0:
                new_col = -new_col - 1
            else:
                new_col = 2 * Ship.columns - new_col - 1
        self.col = new_col


def blast_sequence(aliens, position):
    (rows, column) = position
    Ship.columns = len(aliens[0])
    ships = []
    for (nrow, row) in enumerate(aliens):
        ships.extend((Ship(nrow, ncol, speed) for (ncol, speed) in enumerate(row) if speed))
    (shots, turn) = ([], 0)
    while ships:
        for ship in ships:
            ship.move()
            if ship.row == rows:
                return None
        ships.sort(key=lambda x: x.speed, reverse=True)
        ships.sort(key=lambda x: abs(x.speed), reverse=True)
        ships.sort(key=lambda x: x.row, reverse=True)
        targets = [ship for ship in ships if ship.col == column]
        if targets:
            ships.remove(targets[0])
            shots.append(turn)
        turn += 1
    return shots
