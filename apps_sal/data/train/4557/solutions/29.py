def row_weights(array):
    team1 = []
    team2 = []
    for i,el in enumerate(array):
        if i % 2 == 0:
            team1.append(el)
        else:
            team2.append(el)
    return sum(team1), sum(team2)
