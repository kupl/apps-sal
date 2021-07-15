def rps(p1, p2):
    items = {'rock':0, 'paper':1, 'scissors':2}
    if p1=='rock' and p2=='scissors':
        return "Player 1 won!"
    elif p2=='rock' and p1=='scissors':
        return "Player 2 won!"
    
    if items[p1] > items[p2]:
        return  "Player 1 won!"
    elif items[p1] == items[p2]:
        return "Draw!"
    else:
        return "Player 2 won!"

