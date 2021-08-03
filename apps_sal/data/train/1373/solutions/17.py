for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    l = 0
    r = 0
    ans = 0
    d = {i + 1: 0 for i in range(k)}
    s = set()
    while l <= r < n:
        if len(s) != k:
            s.add(x[r])
            d[x[r]] += 1
            if len(s) != k:
                ans = max(ans, r - l + 1)
            r += 1
        else:
            d[x[l]] -= 1
            if d[x[l]] == 0:
                s.remove(x[l])
            l += 1
    print(ans)
