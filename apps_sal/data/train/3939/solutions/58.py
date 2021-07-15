def rps(p1, p2):
    if p1==p2:
        return "Draw!"
    elif "scissors" in p1:
        if "rock" in p2:
            return "Player 2 won!"
        elif "paper" in p2:
            return "Player 1 won!"
    elif "rock" in p1:
        if "paper" in p2:
            return "Player 2 won!"
        elif "scissors" in p2:
            return "Player 1 won!"
    elif "paper" in p1:
        if "scissors" in p2:
            return "Player 2 won!"
        elif "rock" in p2:
            return "Player 1 won!"
