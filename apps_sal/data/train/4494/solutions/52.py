def points(games):
    result = 0
    for score in games:
        (x, y) = score.split(':')
        if x > y:
            result += 3
        if x == y:
            result += 1
    return result
