def points(games):
    diff = map(lambda x: int(x[0]) - int(x[-1]), games)  # goal difference
    wins = map(lambda x: 3 if x > 0 else x, diff)  # change wins to 3 points
    return sum(list(map(lambda x: 1 if x == 0 else x * (x > 0), wins)))  # change draws and losses to 1 and 0 points
