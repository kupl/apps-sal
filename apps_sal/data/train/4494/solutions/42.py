def points(scores):
    return sum([3 if s[0] > s[2] else 1 for s in scores if s[0] >= s[2]])
