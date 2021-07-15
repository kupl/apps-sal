def candies(s):
    if len(s) <= 1:
        return -1
    m = max(s)
    return sum(m - x for x in s)
