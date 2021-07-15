def candies(s):
    return sum([max(s) - x for x in s]) if len(s) > 1 else -1
