def rps(p1, p2):
    win = [('paper', 'rock'), ('scissors', 'paper'), ('rock', 'scissors')]
    if (p1, p2) in win:
        return "Player 1 won!"
    if (p2, p1) in win:
        return "Player 2 won!"
    else:
        return "Draw!"
