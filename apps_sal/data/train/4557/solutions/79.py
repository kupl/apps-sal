def row_weights(array):
    team1 = 0
    team2 = 0
    for (index, value) in enumerate(array, 1):
        if index % 2 == 0:
            team2 += array[index - 1]
        else:
            team1 += array[index - 1]
    return (team1, team2)
