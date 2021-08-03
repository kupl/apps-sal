for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    x, y = list(map(int, input().split()))
    n -= 1
    m -= 1
    print(max(n - x, x) + max(y, m - y))
