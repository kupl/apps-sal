def candies(s):
    if len(s) == 0 or len(s) == 1:
        return -1
    else:
        return len(s) * max(s) - sum(s)
