def row_weights(array):
    
    team1 = list()
    team2 = list()
    
    for c,e in enumerate(array):
        if c % 2 == 0:
            team1.append(e)
        else:
            team2.append(e)
            
    return (sum(team1), sum(team2))
