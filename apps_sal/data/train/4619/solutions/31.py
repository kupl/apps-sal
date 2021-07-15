def whoseMove(lastPlayer, win):
    return lastPlayer if win else [n for n in ['black', 'white'] if n != lastPlayer][0]
