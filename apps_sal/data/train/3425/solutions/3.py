def word_square(s):
    li = [s.count(i) for i in set(s)]
    t = sum(i for i in li)**0.5
    return int(t) == t and sum(i&1 for i in li) <= t
