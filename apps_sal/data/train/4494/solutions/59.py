def points(games):
    point = 0
    for score in games:
        x, y = map(int, score.split(':'))
        if x > y:
            point += 3
        elif x == y:
            point += 1
    return point
