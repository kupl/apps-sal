def whoseMove(l, w):
    return 'white' if (l=='black' and not w) or ((l=='white' and w)) else 'black'
