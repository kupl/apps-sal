from collections import defaultdict
(n, m, p) = list(map(int, input().split()))
c = [defaultdict(int) for _ in range(n + 1)]
for _ in range(p):
    (i, j) = list(map(int, input().split()))
    c[i][j] += 1
for i in range(1, n + 1):
    if not c[i]:
        print(m - 1)
    else:
        x = m + c[i].get(m, 0)
        v = list(c[i].items())
        v.sort(reverse=True)
        cost = 0
        last_col = m
        ok = True
        for (j, h) in v:
            cost += max(0, last_col - j - 1)
            if j < m:
                x = j + 1 + c[i].get(j + 1, 0)
                if x < j + h:
                    ok = False
                    break
            if j > 1:
                x = h + 1 - c[i].get(j - 1, 0)
                if x < 0:
                    ok = False
                    break
                cost += x
            last_col = j - 1
        if ok:
            print(cost + max(0, last_col - 1))
        else:
            print(-1)
