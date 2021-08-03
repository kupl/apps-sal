def word_pattern(p, s):
    if len(p) != len(s.split()):
        return False
    ss = set([(p[i], c) for i, c in enumerate(s.split())])
    return len(ss) == len(set(p)) == len(set(s.split()))
