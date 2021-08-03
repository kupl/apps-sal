def scramble(s1, s2):
    def ccount(s):
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        return d

    d1 = ccount(s1)
    for c, count in list(ccount(s2).items()):
        if d1.get(c, 0) < count:
            return False
    return True
