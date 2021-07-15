def rps(p1, p2):
    if p1 == p2:
        return 'Draw!' 
    elif p1 == 'rock' or p1 == 'scissors' or p1 == 'paper':
        return 'Player 1 won!' if p2 != 'rock' and p1 == 'scissors' or p2 != 'paper' and p1 == 'rock' or p2 != 'scissors' and p1 == 'paper' else 'Player 2 won!'
    
    



