def row_weights(array):
    team1 = sum([array[i] for i in range(0, len(array), 2)])
    team2 = sum([array[i] for i in range(1, len(array), 2)])

    return (team1, team2)
