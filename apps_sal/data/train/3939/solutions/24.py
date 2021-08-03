def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'

    game_map = {
        ('rock', 'scissors'): 'rock',
        ('scissors', 'paper'): 'scissors',
        ('paper', 'rock'): 'paper'
    }
    winner = game_map.get((p1, p2), False) or game_map.get((p2, p1), False)
    return "Player 1 won!" if p1 == winner else "Player 2 won!"
