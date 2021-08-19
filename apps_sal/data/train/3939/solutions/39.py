def rps(*players):
    result = 'Draw!'
    if players[0] != players[1]:
        if 'rock' in players and (not 'paper' in players):
            winner = players.index('rock') + 1
        elif 'paper' in players and (not 'scissors' in players):
            winner = players.index('paper') + 1
        elif 'scissors' in players and (not 'rock' in players):
            winner = players.index('scissors') + 1
        result = 'Player %s won!' % winner
    return result
