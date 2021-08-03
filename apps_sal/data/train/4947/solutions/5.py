def good_digits(m, d):
    s = str(m)
    res = []
    if len(s) < 2:
        return False
    i = 0
    while i < len(s) - 1:
        if s[i] >= s[i + 1]:
            return False
        if int(s[i + 1]) - int(s[i]) > d:
            return False
        i += 1
    for c in s:
        if c in res:
            return False
        res.append(c)
    return True


def sel_number(n, d):
    cnt = 0
    i = 0
    while i <= n:
        if good_digits(i, d):
            cnt += 1
        i += 1
    return cnt
