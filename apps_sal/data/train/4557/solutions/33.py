def row_weights(array):
    team1 = 0
    team2 = 0
    for x in range(0,len(array)):
        if x % 2 == 0:
            team1 = team1 + array[x]
        else:
            team2 = team2 + array[x]
    return (team1, team2)
