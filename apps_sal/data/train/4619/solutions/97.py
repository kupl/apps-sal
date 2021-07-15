def whoseMove(lastPlayer, win):
    if win==True :
       return lastPlayer
    if win==False :
       if lastPlayer=="black":
          return "white"
       return "black"
