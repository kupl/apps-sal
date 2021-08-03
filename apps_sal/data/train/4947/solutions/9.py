def check(n, d):
    s = str(n)
    if ''.join(sorted(s)) != s:
        return False
    z = s[0]
    for i in xrange(1, len(s)):
        x = s[i]
        if x == z or int(x) - int(z) > d:
            return False
        z = x
    return True


def sel_number(n, d):
    total = 0
    for i in xrange(12, n + 1):
        if check(i, d):
            total += 1
    return total
