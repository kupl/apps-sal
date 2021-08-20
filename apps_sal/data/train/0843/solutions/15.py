test = int(input())
for _ in range(test):
    n = int(input())
    ls = []
    for _ in range(n):
        ls.append(sorted(list(map(int, input().split())), reverse=True))
    m = max(ls[n - 1])
    s = m
    d = 0
    for i in range(n - 2, -1, -1):
        f = 0
        for j in range(n):
            if ls[i][j] < m:
                s += ls[i][j]
                m = ls[i][j]
                f = 1
                break
        if f == 0:
            d = 1
            break
    if d == 0:
        print(s)
    else:
        print(-1)
