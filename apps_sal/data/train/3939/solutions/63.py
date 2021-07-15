def rps(p1, p2):
    rules = {
        'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'
    }
    
    if   rules.get(p1)==p2:  a = 1           # Player 1 won
    elif rules.get(p2)==p1:  a = 2           # Player 2 won
    else:                    return 'Draw!'  # Draw
    
    return f'Player {a} won!'
