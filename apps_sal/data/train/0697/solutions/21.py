for t in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = sum(a[:k])
    minn = s
    for i in range(1, n - k + 1):
        s = s - a[i - 1] + a[i + k - 1]
        if s > minn:
            minn = s
    print(minn)
