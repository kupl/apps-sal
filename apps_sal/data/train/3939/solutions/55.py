def rps(p1, p2):
    x=('rock','scissors','paper')
    y=('rock','scissors','paper')
    if p1 == p2:
        return "Draw!"
    elif p1 == x[0] and p2 == y[1]: 
        return "Player 1 won!" 
    elif p1 == x[1] and p2 == y[2]: 
        return "Player 1 won!" 
    elif p1 == x[2] and p2 == y[0]: 
        return "Player 1 won!" 
    else:
        return "Player 2 won!"
    #your code here

