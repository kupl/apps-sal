def whoseMove(lastPlayer, win):
    if lastPlayer == 'black' and win == False or lastPlayer =='white' and win == True : return 'white'
    elif lastPlayer == 'white' and win == False or lastPlayer =='black' and win == True: return 'black'
