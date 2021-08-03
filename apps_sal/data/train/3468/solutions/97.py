def scramble(s1, s2):
    d1 = {}
    for ch in s1:
        if ch not in d1:
            d1[ch] = 1
        else:
            d1[ch] = d1[ch] + 1
    for ch in s2:
        try:
            if d1[ch] == 0:
                return False
        except KeyError:
            return False
        else:
            d1[ch] = d1[ch] - 1
    return True
