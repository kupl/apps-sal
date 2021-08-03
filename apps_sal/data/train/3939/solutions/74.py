def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    rps = {"rock": 2, "scissors": 1, "paper": 0}
    if p1 == "rock" and p2 == "paper" or p1 == "paper" and p2 == "rock":
        rps["paper"] = 3
    return "Player 1 won!" if rps[p1] > rps[p2] else "Player 2 won!"
