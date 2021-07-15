def points(games):
    points = 0

    for v in games:
        x = int(v[0])
        y = int(v[2])
        if x > y:
            points += 3
        elif x == y:
            points += 1

    return points
