def split_in_parts(s, p):
    l = []
    i = 0
    while i < len(s):
        k = s[i:i + p]
        l.append(k)
        i += p
    res = ' '.join(l)
    return res
