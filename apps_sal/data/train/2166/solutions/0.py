def f():
    return list(map(int, input().split()))[1:]


n = int(input())
(s, p, q) = ([], [], [])
for x in [0, 1]:
    r = f()
    s.append(r)
    t = [len(r)] * n
    t[0] = 0
    p.append(t)
    q.append((x, 0))
while q:
    (x, i) = q.pop()
    y = 1 - x
    for d in s[y]:
        j = (i - d) % n
        if p[y][j] < 1:
            continue
        p[y][j] = -1
        for d in s[x]:
            k = (j - d) % n
            if p[x][k] < 1:
                continue
            p[x][k] -= 1
            if p[x][k] == 0:
                q.append((x, k))
for x in [0, 1]:
    print(*[['Lose', 'Loop', 'Win'][min(q, 1)] for q in p[x][1:]])
