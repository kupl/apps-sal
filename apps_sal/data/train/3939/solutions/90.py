def rps(p1, p2):
    return "Draw!" if p1==p2 else "Player 1 won!" if {'scissors': 'paper', 'paper': 'rock','rock': 'scissors'}.get(p1) == p2 else "Player 2 won!"
