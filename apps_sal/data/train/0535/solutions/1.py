
def solve(N, M, x, y):
    n, m = min(N, M), max(N, M)

    count = ((n - 1) * n * (2 * n - 1) // 3 + (m - n + 1) * n**2) * 2
    p1, p2 = min(x - 1, y - 1), min(N - x, M - y)
    r1, r2 = min(M - y, x - 1), min(N - x, y - 1)
    count += (n + m) * n * m

    count -= p1 + p2 + r1 + r2 + n + m + 2

    count += (n * m) - (p1 + p2 + r1 + r2 + n + m - 1)

    count -= (n * m - 1) * 3
    tot = (n * m - 1) * n * m - count
    tot += 2 * (p1 * p2 + r1 * r2 + (x - 1) * (N - x) + (y - 1) * (M - y))

    return tot


for _ in range(int(input())):

    n, m, x, y = list(map(int, input().split()))
    print(solve(n, m, x, y))
