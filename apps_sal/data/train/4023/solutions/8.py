def high(s):
    return max( (sum(ord(c) - 96 for c in x), x) for x in s.split() )[1]


