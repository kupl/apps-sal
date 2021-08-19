from collections import Counter
for _ in range(int(input())):
    s = input()
    c = Counter(list(s))
    if len(c) == 1:
        print(0)
    else:
        m = min(c['b'], c['g'])
        ma = max(c['b'], c['g'])
        l = (ma - m + 1) // 2
        r = (ma - m + 1) // 2 + (ma - m + 1) % 2
        res = l * (l + 1) // 2
        re = res
        for i in range(1, m):
            res += 2 * l + 1
            re += res
            l += 1
        res2 = r * (r + 1) // 2
        re += res2
        for i in range(1, m):
            res2 += 2 * r + 1
            re += res2
            r += 1
        print(re)
