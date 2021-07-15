def whoseMove(last, win):
    if win==True:
        return last
    else:
        return "black" if last=="white" else "white"
