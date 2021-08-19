t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    k = []
    for i in range(n):
        for j in range(m):
            k.append([l[i][j], i, j])
    k.sort()
    s = []
    for i in range(n):
        s.append([0] * m)
    for i in k:
        x = i[1]
        y = i[2]
        s[x][y] = 1
        c = 1
        for j in range(x + 1, n):
            s[j][y] = 0
            for b in range(y - 1, max(y - c - 1, -1), -1):
                s[j][b] = 0
            for b in range(y + 1, min(m, y + c + 1)):
                s[j][b] = 0
            c += 1
    for i in s:
        print(''.join(map(str, i)))
