def points(games):

    points = 0

    for game in games:
        x, y = game.split(':')
        if x > y:
            points += 3
        if x < y:
            points += 0
        if x == y:
            points += 1

    return points
