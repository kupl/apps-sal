def rps(p1, p2):
    moves = {'scissors':'paper', 'paper':'rock', 'rock':'scissors'}
    if p1 == p2: return "Draw!"
    if moves[p1] == p2: return "Player 1 won!"
    return "Player 2 won!"
