nCr = [[0 for x in range(1001)] for x in range(1001)]
for i in range(0, 1001):
    nCr[i][0] = 1
    nCr[i][i] = 1
for i in range(1, 1001):
    for j in range(1, 1001):
        if i != j:
            nCr[i][j] = nCr[i - 1][j] + nCr[i - 1][j - 1]
t = eval(input())
for _ in range(0, t):
    (s, n, m, k) = list(map(int, input().split(' ')))
    y = 0
    if s == n:
        print('1.000000')
        continue
    if k > m or k > n:
        print('0.000000')
        continue
    total = float(nCr[s - 1][n - 1])
    if m > n:
        z = m
    else:
        z = n
    for i in range(k, z):
        y += nCr[m - 1][i] * nCr[s - m][n - i - 1]
    print('%.6f' % float(y / total))
