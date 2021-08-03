def points(games): return sum(map(lambda p: 3 if p[0] > p[2] else(1 if p[0] == p[2] else 0), games))
