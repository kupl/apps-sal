t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        l.append(input())
    li = []
    for i in range(n):
        for j in range(m):
            if(l[i][j] == '1'):
                li.append((i + 1, j + 1))
    di = [0 for i in range(n + m - 2)]
    for x in range(len(li)):
        for y in li[x + 1:]:
            z = li[x]
            distance = abs(z[0] - y[0]) + abs(z[1] - y[1])
            di[distance - 1] = di[distance - 1] + 1
    for x in di:
        print(x, end=' ')
    print()
