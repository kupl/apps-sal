def solve():
    (n, m) = map(int, input().split())
    a = [0 for x in range(n)]
    b = [0 for x in range(n)]
    for i in range(m):
        (row, col) = map(int, input().split())
        row -= 1
        col -= 1
        a[row] += 1
        b[col] += 1
    res = 0
    for i in range(1, n - 1):
        if a[i] == 0:
            res += 1
        if b[i] == 0:
            res += 1
        if a[i] == 0 and b[i] == 0 and (i == n - i - 1):
            res -= 1
    print(res)


solve()
