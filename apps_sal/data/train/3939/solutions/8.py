def rps(p1, p2):
    d1 = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]
    return 'Draw!' if p1 == p2 else "Player {} won!".format(1 if (p1, p2) in d1 else 2)
