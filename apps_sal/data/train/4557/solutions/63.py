def row_weights(array):
    team1 = []
    team2 = []
    for i in range(len(array)):
        if i % 2 == 0:
            team1.append(array[i])
        else:
            team2.append(array[i])
    weight_team1 = sum(team1)
    weight_team2 = sum(team2)
    return (weight_team1, weight_team2)
