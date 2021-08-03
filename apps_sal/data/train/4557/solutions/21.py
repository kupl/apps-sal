def row_weights(array):
    team_1 = []
    team_2 = []
    for i, el in enumerate(array):
        if i % 2 == 0:
            team_1.append(el)
        else:
            team_2.append(el)
    return sum(team_1), sum(team_2)
