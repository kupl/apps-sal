def fx(s, n, xsum):
    sub = [[None for x in range(n + 2)]for y in range(xsum + 2)]
    for i in range(n + 1):
        sub[0][i] = True
    for i in range(1, xsum + 1):
        sub[i][0] = False
    for i in range(1, xsum + 1):
        for j in range(1, n + 1):
            sub[i][j] = sub[i][j - 1]
            if i >= s[j - 1]:
                sub[i][j] = sub[i][j] or sub[i - s[j - 1]][j - 1]
    if sub[xsum][n]:
        print('Yes')
    else:
        print('No')


n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
for _ in range(t):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a[q[1] - 1] = q[2]
        continue
    if q[0] == 2:
        w = a[q[1] - 1:q[2]]
        a[q[1] - 1:q[2]] = w[::-1]
        continue
    if q[0] == 3:
        e = a[q[1] - 1:q[2]]
        if q[3] < min(e) or q[3] > sum(e):
            print('No')
            continue
        if q[3] in e:
            print('Yes')
            continue
        fx(e, len(e), q[3])
