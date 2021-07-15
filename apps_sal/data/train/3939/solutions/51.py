def rps(p1, p2):
    if p1 == 'rock':
        if p2 == 'paper':
            return 'Player 2 won!'
        elif p2 == 'scissors':
            return 'Player 1 won!'
        else:
            return 'Draw!'
    elif p1 == 'paper':
        if p2 == 'rock':
            return 'Player 1 won!'
        elif p2 == 'scissors':
            return 'Player 2 won!'
        else:
            return 'Draw!'
    else:
        if p2 == 'rock':
            return 'Player 2 won!'
        elif p2 == 'paper':
            return 'Player 1 won!'
        else:
            return 'Draw!'
