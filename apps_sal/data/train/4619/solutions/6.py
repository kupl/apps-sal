def whoseMove(lastPlayer, win):
  otherPlayer = "black" if lastPlayer == "white" else "white"
  return lastPlayer if win else otherPlayer

