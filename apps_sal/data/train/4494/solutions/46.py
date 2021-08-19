def points(games):
    scores = (game.split(':') for game in games)
    return sum(([0, 1, 3][(x >= y) + (x > y)] for (x, y) in scores))
