corr = lambda x, y: 1 <= x <= n and 1 <= y <= m

T = int(input())
a = []
while T:
    a.append(T % 6)
    T //= 6
L = len(a)
n = m = L * 2 + 2
ans = [(1, 2, 2, 2), (2, 1, 2, 2)]
f = [[1] * 9 for i in range(7)]
f[1][2] = f[2][2] = f[2][6] = f[3][5] = 0
f[4][5] = f[4][6] = f[5][2] = f[5][5] = f[5][6] = 0
p = [0] * 9
p[1] = 3, 1, 3, 2
p[2] = 4, 1, 4, 2
p[3] = 4, 2, 5, 2
p[4] = 4, 3, 5, 3
p[5] = 1, 3, 2, 3
p[6] = 1, 4, 2, 4
p[7] = 2, 4, 2, 5
p[8] = 3, 4, 3, 5
for i in range(L):
    bit = a[L - i - 1]
    for j in range(1, 9):
        if not f[bit][j]: continue
        x1, y1, x2, y2 = p[j]; D = 2 * i
        x1 += D; y1 += D; x2 += D; y2 += D
        if corr(x2, y2): ans.append((x1, y1, x2, y2))
for i in range(L - 1):
    x1, y1 = 5 + i * 2, 1 + i * 2
    x2, y2 = 1 + i * 2, 5 + i * 2
    ans.append((x1, y1, x1 + 1, y1))
    ans.append((x1, y1 + 1, x1 + 1, y1 + 1))
    ans.append((x2, y2, x2, y2 + 1))
    ans.append((x2 + 1, y2, x2 + 1, y2 + 1))
print(n, m)
print(len(ans))
[print(*i) for i in ans]

