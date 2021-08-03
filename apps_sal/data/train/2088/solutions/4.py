n = int(input())
t = tuple(map(int, input().split()))
m = [[1] * n for i in range(n + 1)]
for d in range(2, n + 1):
    for i in range(n - d + 1):
        m[d][i] = min(m[x][i] + m[d - x][i + x] for x in range(1, d))
        if t[i] == t[i + d - 1]:
            m[d][i] = min(m[d][i], m[d - 2][i + 1])
print(m[n][0])
