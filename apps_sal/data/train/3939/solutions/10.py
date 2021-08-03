def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    return "Player 1 won!" if (p1[0] + p2[0]) == "sp" or (p1[0] + p2[0]) == "rs" or (p1[0] + p2[0]) == "pr" else "Player 2 won!"
