def whoseMove(lastPlayer, win):
    winlose = ['black', 'white']
    winlose.remove(lastPlayer)
    return lastPlayer * win + winlose[0] * (not win)
