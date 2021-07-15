def whoseMove(lastPlayer, win):
    print(lastPlayer, win)
    return lastPlayer if win else 'white' * (lastPlayer != 'white') + 'black' * (lastPlayer != 'black')
