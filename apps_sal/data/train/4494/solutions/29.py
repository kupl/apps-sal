def points(games):
    points = 0
    for game in games:
        x, y = game.split(":")
        points += [0, 1, 3][(x >= y) + (x > y)]
    return points
