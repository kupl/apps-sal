def score_throws(r):
    if not r:
        return 0
    if all(i < 5 for i in r):
        return len(r) * 10 + 100
    return len([i for i in r if i <= 10 and i >= 5]) * 5 + len([i for i in r if i < 5]) * 10
