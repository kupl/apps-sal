for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    n -= l.count(0)
    p = l.count(2)
    k = l.count(1)
    n -= k
    ans = n * (n - 1) // 2
    if p > 1:
        ans -= (p - 1) * p // 2
    print(ans)
