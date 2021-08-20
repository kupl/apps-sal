def blast_sequence(aliens, position):
    board_len = len(aliens[0])
    aliens = {(x, y, steps) for (y, lst) in enumerate(aliens) for (x, steps) in enumerate(lst) if steps != 0}
    solution = []
    turn = -1
    while all((alien[1] != position[0] for alien in aliens)) and aliens:
        turn += 1
        aliens = {(alien[0] + alien[2], alien[1], alien[2]) if 0 <= alien[0] + alien[2] < board_len else (-1 * (alien[0] + alien[2] + 1) % board_len, alien[1] + 1, alien[2] * -1) for alien in aliens}
        alien = max((alien for alien in aliens if alien[0] == position[1]), key=lambda alien: (alien[1], abs(alien[2]), alien[2]), default=None)
        if alien:
            aliens ^= {alien}
            solution.append(turn)
    return solution if not aliens else None
