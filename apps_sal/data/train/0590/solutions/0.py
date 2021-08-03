for _ in range(int(input())):
    n, x, m = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(m):
        for i in range(1, n):
            a[i] = a[i] + a[i - 1]
    print(a[x - 1] % (10**9 + 7))
