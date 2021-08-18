for _ in range(int(input())):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()
    if k <= n // 2:
        s1 = sum(w[:k])
        s2 = sum(w[k:])
        print(abs(s2 - s1))
    else:
        s1 = sum(w[n - k:])
        s2 = sum(w[:n - k])
        print(abs(s2 - s1))
