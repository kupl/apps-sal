def points(games):
    points = 0
    for a in games:
        if a[0] > a[2]:
            points += 3
        elif a[0] == a[2]:
            points += 1
    return points
