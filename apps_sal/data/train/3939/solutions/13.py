def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    favourable_matchups = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    return 'Player 1 won!' if favourable_matchups[p1] == p2 else 'Player 2 won!'
