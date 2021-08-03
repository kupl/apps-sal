def rps(p1, p2):
    result = [p1, p2]
    if result[0] == 'rock':
        if result[1] == 'paper':
            return 'Player 2 won!'
        if result[1] == 'rock':
            return 'Draw!'
        if result[1] == 'scissors':
            return 'Player 1 won!'
    elif result[0] == 'paper':
        if result[1] == 'rock':
            return 'Player 1 won!'
        if result[1] == 'paper':
            return 'Draw!'
        if result[1] == 'scissors':
            return 'Player 2 won!'
    elif result[0] == 'scissors':
        if result[1] == 'scissors':
            return 'Draw!'
        if result[1] == 'paper':
            return "Player 1 won!"
        if result[1] == 'rock':
            return 'Player 2 won!'
