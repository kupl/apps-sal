import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

for _ in range(inp()):
    n, m = ip()
    x = [ip() for i in range(n)]
    s = input().strip()
    p, q = ip()
    ans = 0
    for i in range(n + m - 1):
        dt = {0: 0, 1: 0}
        if i < m:
            row, col = 0, i
        else:
            row, col = i - m + 1, m - 1
        while col >= 0 and row < n:
            dt[x[row][col]] += 1
            col -= 1
            row += 1
        if s[i] == '0':
            t = min(dt[1] * p, q + dt[0] * p)
        elif s[i] == '1':
            t = min(dt[0] * p, q + dt[1] * p)
        ans += t
    print(ans)
