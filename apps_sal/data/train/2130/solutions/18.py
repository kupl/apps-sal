(k, md, s, res) = (int(input()), 1000000007, int(input()), 1)
c = [[1] + [0] * 1000 for i in range(1001)]
for i in range(1, 1001):
    for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % md
for i in range(1, k):
    x = int(input())
    s += x
    res = res * c[s - 1][x - 1] % md
print(res)
