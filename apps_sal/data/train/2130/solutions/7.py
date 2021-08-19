pt = []
for i in range(1000):
    pt.append([0] * (i + 1))
    pt[i][0] = pt[i][i] = 1
    for j in range(1, i):
        pt[i][j] = pt[i - 1][j - 1] + pt[i - 1][j]
(k, s, v) = (int(input()), int(input()), 1)
for i in range(1, k):
    c = int(input())
    v = v * pt[s + c - 1][c - 1] % 1000000007
    s += c
print(v)
