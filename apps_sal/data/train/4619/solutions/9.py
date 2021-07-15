def whoseMove(lastPlayer, win):
    op = ['black', 'white']
    op.remove(lastPlayer)
    return lastPlayer if win else op[0]
