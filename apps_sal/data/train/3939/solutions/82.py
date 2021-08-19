def rps(p1, p2):
    result = ''
    if p1 == 'rock' and p2 == 'scissors':
        result = 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'paper':
        result = 'Player 1 won!'
    elif p1 == 'paper' and p2 == 'rock':
        result = 'Player 1 won!'
    elif p2 == 'rock' and p1 == 'scissors':
        result = 'Player 2 won!'
    elif p2 == 'scissors' and p1 == 'paper':
        result = 'Player 2 won!'
    elif p2 == 'paper' and p1 == 'rock':
        result = 'Player 2 won!'
    else:
        result = 'Draw!'
    return result
