def encode(s):
    if not s:
        return("", 0)
    acc = []
    for i in range(len(s)):
        acc.append(s[-i:] + s[:-i])
    acc = sorted(acc)
    r = []
    for a in acc:
        r.append(a[-1])
    return("".join(r), acc.index(s))


def decode(s, n):
    if not s:
        return ""
    res = [""] * len(s)
    for _ in range(len(s)):
        u = []
        for i in range(len(s)):
            u.append(s[i] + res[i])
        res = sorted(u)
    return res[n]
