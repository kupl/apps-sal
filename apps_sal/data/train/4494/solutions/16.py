def points(games):
    points = 0
    for game in games:
        x = int(game[0])
        y = int(game[2])
        if x > y:
            points += 3
        elif x == y:
            points += 1
    return points
