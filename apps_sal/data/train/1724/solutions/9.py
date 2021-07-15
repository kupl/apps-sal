def blast_sequence(aliens_input, position):
    SHIP_X = position[1]
    HEIGHT = position[0] + 1
    WIDTH = len(aliens_input[0])
    turn = 0
    seq = []
    class Alien:
        def __init__(self, coords, cell):
            self.x, self.y = coords
            self.moves = abs(cell)
            self.dir = 1 if cell > 0 else -1
    aliens = [Alien((x, y), cell) for y, row in enumerate(aliens_input) for x, cell in enumerate(aliens_input[y]) if cell]
    
    def moveAlien(alien):
        for i in range(alien.moves):
            if alien.dir == -1 and alien.x == 0 or alien.dir == 1 and alien.x == WIDTH - 1:
                alien.dir *= -1
                alien.y += 1
                if alien.y == HEIGHT - 1:
                    return True
            else:
                alien.x += alien.dir
    def moveAliens():
        for alien in aliens:
            if moveAlien(alien):
                return True
    def fireCannon():
        aliensInLine = list(filter(lambda a: a.x == SHIP_X, aliens))
        if not aliensInLine:
            return
        targetAlien = None
        for alien in aliensInLine:
            if (
                not targetAlien or
                alien.y > targetAlien.y or
                alien.y == targetAlien.y and (
                    alien.moves > targetAlien.moves or
                    alien.moves == targetAlien.moves and alien.dir == 1
                )
            ):
                targetAlien = alien
        aliens.remove(targetAlien)
        seq.append(turn - 1)
    def makeTurn():
        nonlocal turn
        turn += 1
        if moveAliens():
            return True
        fireCannon()
    
    while aliens:
        if makeTurn():
            return None
    return seq
