def spot_diff(s1, s2):
    r = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            r.append(i)
    return r
