def whoseMove(lastPlayer, win):
    return {"white", "black"}.difference({lastPlayer}).pop() if not win else lastPlayer
