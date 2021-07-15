def points(games):
    return sum(3 if x > y else 0 if x < y else 1 for x, y in (score.split(":") for score in games))
