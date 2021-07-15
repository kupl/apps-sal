def points(games):
    def convert(game):
        x, y = int(game[0]), int(game[2])
        return 3 if x > y else 1 if x == y else 0
    return sum(convert(game) for game in games)
