def row_weights(array):
    team_1 = []
    team_2 = []
    for i, num in enumerate(array):
        if i % 2 == 0:
            team_1.append(num)
        if i % 2 == 1:
            team_2.append(num)
    return sum(team_1), sum(team_2)
