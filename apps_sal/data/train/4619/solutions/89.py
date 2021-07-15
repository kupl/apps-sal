def whoseMove(lastPlayer, win):
    if lastPlayer=='white'and win:
        return "white"
    elif lastPlayer=='black' and not win:
        return 'white'
    elif lastPlayer=='white' and not win:
        return 'black'
    elif lastPlayer=='black' and win:
        return 'black'
