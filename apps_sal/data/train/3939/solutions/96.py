def rps(p1, p2):
    win = {"scissors":"rock", "paper":"scissors", "rock":"paper"}
    return "Draw!" if p1 == p2 else "Player 2 won!" if p2 == win[p1] else "Player 1 won!" 
