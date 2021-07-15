def slogans(p, r):
    ans = 0
    while r:
        ans += 1
        for i in range(len(p)):
            if r.startswith(p[i:]):
                r = r[len(p) - i:]
                break
    return ans
