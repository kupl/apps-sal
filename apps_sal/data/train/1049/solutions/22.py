for _ in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    length = len(set(a))
    tot = sum(a[:k - 1])
    tmp = 0
    ans = 0
    for i in range(k - 1, n):
        tot += a[i] - tmp
        if len(set(a[i - k + 1:i + 1])) == length:
            ans = max(ans, tot)
        tmp = a[i - k + 1]
    print(ans)
