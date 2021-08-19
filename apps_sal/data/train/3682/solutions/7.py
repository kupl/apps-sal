def common_len(s1, s2):
    (n, m) = (len(s1), len(s2))
    i = 0
    for c1 in s1:
        if i >= len(s2):
            break
        elif c1 == s2[i]:
            i += 1
    return i


def string_constructing(a, s):
    r = []
    c = 0
    p = 0
    while p < len(s):
        l = common_len(a, s[p:p + len(a)])
        c += 1 + len(a) - l
        p += l
    return c
