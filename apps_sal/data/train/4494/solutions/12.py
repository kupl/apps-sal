def score_game(x, y):
    if x > y:
        return 3
    if x < y:
        return 0
    return 1


def points(games):
    return sum(score_game(*game.split(':')) for game in games)
