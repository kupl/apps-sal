def buy_newspaper(s1, s2):
    t, i = 0, len(s1)
    for c in s2:
        i = s1.find(c, i) + 1
        if not i:
            t += 1
            i = s1.find(c) + 1
            if not i:
                return -1
    return t
