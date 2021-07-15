def candies(s):
    return -1 if len(s) < 2 else len(s) * max(s) - sum(s)
