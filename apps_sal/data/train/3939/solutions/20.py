def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1, p2) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
