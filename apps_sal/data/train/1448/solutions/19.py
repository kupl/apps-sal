for _ in range(int(input())):
    (a, d, k, n, inc) = list(map(int, input().split()))
    ans = a
    for i in range(2, n + 1):
        ans += d
        if i % k == 0 and i >= k:
            d += inc
    print(ans)
