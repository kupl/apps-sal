def whoseMove(lastPlayer, win):
    return ['black','white'][not win] if lastPlayer == 'black' else ['black','white'][win]
