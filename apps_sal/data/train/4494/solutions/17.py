def points(games):
    points = 0
    for i in range(len(games)):
        if games[i][0] > games[i][2]:
            points += 3
        elif games[i][0] == games[i][2]:
            points += 1
    return points
