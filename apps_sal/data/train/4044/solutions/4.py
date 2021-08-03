def string_suffix(s):
    def sim(s1, s2): return ([c1 == c2 for c1, c2 in zip(s1, s2)] + [False]).index(False)
    return sum(sim(s, s[i:]) for i in range(len(s)))
