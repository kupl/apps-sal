for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = 0
    sm = 0
    ans = 0
    d = dict()
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
        if d[a[i]] == 1:
            sm += 1
        if sm == k:
            ans = max(ans, i - p)
            while sm == k:
                d[a[p]] = d[a[p]] - 1
                p += 1
                if d[a[p - 1]] == 0:
                    sm -= 1
                    break
    ans = max(ans, n - p)
    if ans == 0:
        ans = n
    print(ans)
