mm = 1000000007
MAXN = 4001
comb = [[0] * MAXN]
comb[0][0] = 1
for i in range(1, MAXN):
    comb.append([0] * MAXN)
    comb[i][0] = 1
    for j in range(1, i + 1):
        comb[i][j] = comb[i - 1][j] + comb[i - 1][j - 1]
        comb[i][j] %= mm
p2 = [1, 2]
for i in range(2, 4001):
    p2.append(p2[-1] * 2 % mm)
t = int(input())
while t > 0:
    (n, m) = [int(x) for x in input().split()]
    while m > 0:
        (a, b) = [int(x) for x in input().split()]
        if b > a:
            print(0)
        else:
            r = comb[a - 1][b - 1]
            print(r * p2[n - a] % mm)
        m -= 1
    t -= 1
