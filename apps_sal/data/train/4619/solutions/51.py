def whoseMove(lp, abool):
    if lp == "black":
        if abool == True:
            ansr = "black"
        else:
            ansr = "white"
    if lp == "white":
        if abool == True:
            ansr = "white"
        else:
            ansr = "black"
    return ansr
