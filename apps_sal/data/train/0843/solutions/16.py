for u in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(sorted(list(map(int, input().split())), reverse=True))
    m = max(l[n - 1])
    s = m
    d = 0
    for i in range(n - 2, -1, -1):
        f = 0
        for j in range(n):
            if l[i][j] < m:
                s += l[i][j]
                m = l[i][j]
                f = 1
                break
        if f == 0:
            d = 1
            break
    if d == 0:
        print(s)
    else:
        print(-1)
