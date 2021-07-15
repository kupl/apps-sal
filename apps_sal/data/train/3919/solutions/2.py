def shuffled_array(s):
    s.pop(s.index(sum(s) /2))
    return sorted(s)
