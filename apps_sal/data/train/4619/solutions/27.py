def whoseMove(lastPlayer, win):
    return ('white', 'black')[win ^ lastPlayer.startswith('w')]
