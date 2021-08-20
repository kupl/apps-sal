def whoseMove(lastPlayer, win):
    l = lastPlayer
    w = win
    if l == 'white' and w == False:
        return 'black'
    if l == 'white' and w == True:
        return 'white'
    if l == 'black' and w == True:
        return 'black'
    if l == 'black' and w == False:
        return 'white'
