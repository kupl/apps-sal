from collections import Counter

def odd_one_out(s):
    d = Counter(reversed(s))
    return [x for x in d if d[x] % 2][::-1]
