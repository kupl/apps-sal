for T in range(int(input())):
    n, m, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    v = [[0 for x in range(m)] for x in range(n)]
    for i in range(n):
        v[i] = a[i].copy()
    for i in range(n):
        for j in range(1, m):
            a[i][j] += a[i][j - 1]
    for i in range(m):
        for j in range(1, n):
            v[j][i] += v[j - 1][i]
    maxx = 0
    for i in range(n):
        for j in range(k - 1, m):
            if j == k - 1:
                maxx = max(maxx, a[i][j])
            else:
                maxx = max(maxx, a[i][j] - a[i][j - k])
    for i in range(m):
        for j in range(k - 1, n):
            if j == k - 1:
                maxx = max(maxx, v[j][i])
            else:
                maxx = max(maxx, v[j][i] - v[j - k][i])
    print(maxx)
