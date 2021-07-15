beats = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    
    if beats[p1] == p2:
        return 'Player 1 won!'
    
    return 'Player 2 won!'

