def points(games):
    def score(x):
        if x[0] > x[2]:
            return 3
        elif x[0] < x[2]:
            return 0
        else:
            return 1
    return sum(score(x) for x in games)
