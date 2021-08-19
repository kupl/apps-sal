import sys
ip = sys.stdin


def solve(C, n, x):
    if n == 1:
        return (1, 0)
    (b1, b2) = (1, 1)
    (a, b) = (C[0], C[-1])
    while b1 + b2 < n:
        if a < b * x:
            a += C[b1]
            b1 += 1
        elif a > b * x:
            b2 += 1
            b += C[n - b2]
        elif b1 >= b2:
            a += C[b1]
            b1 += 1
        else:
            b2 += 1
            b += C[b2]
    return (b1, b2)


t = int(ip.readline())
for _ in range(t):
    n = int(ip.readline())
    C = list(map(int, ip.readline().split()))
    x = int(ip.readline())
    ans = solve(C, n, x)
    print(*ans)
