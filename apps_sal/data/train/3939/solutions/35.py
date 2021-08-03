def rps(p1, p2):
    values = {'rock': 0, 'scissors': 1, 'paper': 2}
    if (values[p1] - values[p2]) % 3 == 0:
        return 'Draw!'
    elif (values[p1] - values[p2]) % 3 == 2:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
