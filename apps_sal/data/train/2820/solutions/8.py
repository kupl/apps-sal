def spot_diff(s1, s2):
    ret = []
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            ret.append(i)
    return ret
