def candies(s):
    return max(s) * len(s) - sum(s) if len(s) > 1 else -1
