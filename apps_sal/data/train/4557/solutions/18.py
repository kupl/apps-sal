def row_weights(array):
    team1 = [el for i, el in enumerate(array) if i % 2 == 0]
    team2 = [el for i, el in enumerate(array) if i % 2 != 0]
    return sum(team1), sum(team2)
