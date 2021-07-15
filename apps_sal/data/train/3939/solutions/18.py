BEATS = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def rps(p1, p2):
    return 'Draw!' if p1 == p2 else __winner(p1, p2)

def __winner(p1, p2): 
    return 'Player 1 won!' if BEATS[p1] == p2 else 'Player 2 won!'

