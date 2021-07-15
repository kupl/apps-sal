def row_weights(array):
    team_1 = []
    team_2 = []
    
    for idx, num in enumerate(array):
        if idx % 2 != 0:
            team_2.append(num)
        else:
            team_1.append(num)
            
    return sum(team_1), sum(team_2)
