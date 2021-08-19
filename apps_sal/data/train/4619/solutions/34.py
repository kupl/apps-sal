def whoseMove(p, win):
    return 'white' if p == 'white' and win or (p == 'black' and (not win)) else 'black'
