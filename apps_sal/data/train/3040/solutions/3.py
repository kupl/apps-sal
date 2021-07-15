def candies(s):
    return sum([max(s)-i for i in s]) if len(s) > 1 else -1
