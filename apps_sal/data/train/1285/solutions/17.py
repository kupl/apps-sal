t = int(input())
for i in range(t):
    n = int(input())
    mat = []
    for i in range(n):
        l = list(map(int, input().split()))
        mat.append(l)
    ans = []
    for x in range(n - 1, -1, -1):
        s = 0
        for (i, j) in zip(range(n), range(x, n)):
            s += mat[i][j]
        ans.append(s)
    for y in range(1, n):
        s1 = 0
        for (i, j) in zip(range(y, n), range(n)):
            s1 += mat[i][j]
        ans.append(s1)
    print(max(ans))
