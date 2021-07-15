def whoseMove(lastPlayer, win):
    return lastPlayer if win else list({'black', 'white'} - {lastPlayer})[0]
