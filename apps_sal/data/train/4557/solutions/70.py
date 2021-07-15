def row_weights(array):
    team1 = 0
    team2 = 0
    
    i = 0
    while i < len(array):
        if i % 2 == 0:
            team1 = team1 + array[i]
        else:
            team2 = team2 + array[i]
        i = i + 1
    
    return (team1,team2)
