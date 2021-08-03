def whoseMove(lp, win):
    if win:
        return lp
    else:
        return [i for i in ['black', 'white'] if i not in lp][0]
