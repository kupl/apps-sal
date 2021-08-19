def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'


'    if p1 == p2:\n        return "Draw!"\n    elif p1[0].lower == "s" and p2[0].lower == "p":\n        return "Player 1 won!"\n    elif p1[0].lower == "r" and p2[0].lower == "s":\n        return "Player 1 won!"\n    elif p1[0].lower == "p" and p2[0].lower == "r":\n        return "Player 1 won!"\n    else:\n        return "Player 2 won!"\n'
r1 = 'rock'
r2 = 'scissors'
print(rps(r1, r2))
