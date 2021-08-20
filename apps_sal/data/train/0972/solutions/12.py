try:
    (n, k) = map(int, input().split())
    l = []
    for i in range(n):
        l.append(int(input()))
    l.sort()
    res = l[0 + k - 1] - l[0]
    for i in range(n - k + 1):
        d = l[i + k - 1] - l[i]
        res = min(res, d)
    print(res)
except EOFError as e:
    pass
