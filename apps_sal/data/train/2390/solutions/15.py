T = int(input())
for i in range(T):
    n = int(input())
    s = [list(map(int, input().split()))]
    p = {}
    q = {}
    for it in s:
        for j in range(n):
            if it[j] in q:
                q[it[j]] += 1
            else:
                q[it[j]] = 1
    for j in range(1, n + 1):
        if j in q:
            if q[j] in p:
                p[q[j]] += 1
            else:
                p[q[j]] = 1
    x = n
    ans = 0
    cnt = 0
    while x > 0:
        if x in p:
            cnt += p[x]
        if cnt > 0:
            ans += x
            cnt -= 1
        x -= 1
    print(ans)
    p.clear()
    q.clear()
    s.clear()
