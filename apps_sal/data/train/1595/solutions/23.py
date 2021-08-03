from sys import stdin


def filtera(p):
    p = p.replace('w', '1')
    p = p.replace('b', '0')
    return p


def filtern(q):
    q = q.replace('+', '1')
    q = q.replace('-', '0')
    return q


mod = 10**9 + 7
inp = stdin.read().split()
x = 0
for _ in range(int(inp[x])):
    x += 1
    m = int(filtera(inp[x]), 2)
    x += 1
    n = int(inp[x])
    arr = []
    for _ in range(n):
        x += 1
        k = int(filtern(inp[x]), 2)
        arr.append(k)
    d = [[0] * (1025) for _ in range(2)]
    d[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1024):
            d[i % 2][j] = (d[(i - 1) % 2][j] + d[(i - 1) % 2][j ^ arr[i - 1]]) % mod
    if n % 2:
        print(d[1][m] % mod)
    else:
        print(d[0][m] % mod)
