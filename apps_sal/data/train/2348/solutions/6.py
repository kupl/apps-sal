def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    L = int(input())
    dp = [[0] * 20 for _ in range(n)]
    for i in range(n):
        l, r = i, n
        while l < r:
            mid = (l + r) >> 1
            if arr[mid] - arr[i] <= L:
                l = mid + 1
            else:
                r = mid
        dp[i][0] = r - 1

    for j in range(1, 20):
        for i in range(n):
            dp[i][j] = dp[dp[i][j - 1]][j - 1]

    q = int(input())
    for _ in range(q):
        x, y = list(map(int, input().split()))
        x -= 1
        y -= 1
        if x > y:
            x, y = y, x
        tmp = 0
        for j in range(19, -1, -1):
            if dp[x][j] < y:
                tmp += 1 << j
                x = dp[x][j]
        print((tmp + 1))


solve()
