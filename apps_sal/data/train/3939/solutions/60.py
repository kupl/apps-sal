def rps(p1, p2):
    print(p1, p2)
    if p1 == p2:
        return "Draw!"
    if p1 == 'scissors' and p2 != 'rock':
        return "Player 1 won!"
    if p1 == 'scissors' and p2 == 'rock':
        return "Player 2 won!"
    if p2 == 'scissors' and p1 != 'rock':
        return "Player 2 won!"
    if p2 == 'scissors' and p1 == 'rock':
        return "Player 1 won!"
    if p1 == "paper" and p2 != 'scissors':
        return "Player 1 won!"
    if p1 == 'paper' and p2 == 'scissors':
        return "player 2 won!"
    if p2 == 'paper' and p1 != 'scissors':
        return "Player 2 won!"
    if p2 == 'paper' and p1 == 'scissors':
        return "player 1 won!"
