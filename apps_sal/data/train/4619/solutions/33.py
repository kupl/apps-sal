def whoseMove(l, w):
    return 'bwlhaictke'[(l[0] == 'b') != w::2]
