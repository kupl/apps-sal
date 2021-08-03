def points(games):
    p = 0
    for game in games:
        x, y = game.split(':')
        p += 3 if x > y else 0 if x < y else 1
    return p
