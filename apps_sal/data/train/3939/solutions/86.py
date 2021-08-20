def rps(p1, p2):
    if p1[0] == 'r' and p2[0] == 's':
        soluzione = 'Player 1 won!'
    elif p1[0] == 'p' and p2[0] == 's':
        soluzione = 'Player 2 won!'
    elif p1[0] == 'r' and p2[0] == 'p':
        soluzione = 'Player 2 won!'
    elif p1[0] == 'p' and p2[0] == 'r':
        soluzione = 'Player 1 won!'
    elif p1[0] == 's' and p2[0] == 'r':
        soluzione = 'Player 2 won!'
    elif p1[0] == 's' and p2[0] == 'p':
        soluzione = 'Player 1 won!'
    else:
        soluzione = 'Draw!'
    return soluzione
