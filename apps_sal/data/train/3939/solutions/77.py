def rps(p1, p2):
    score = {"rock": 1, "paper": 2, "scissors": 3}
    if p1 == p2:
        return "Draw!"
    elif (score[p1] - score[p2]) % 3 > 1:
        return "Player 2 won!"
    else:
        return "Player 1 won!"
