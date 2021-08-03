for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    days = 0
    i = 0
    while i < n:
        if a[i] <= m:
            m = max(2 * a[i], m)
            days += 1
            i += 1
        else:
            m *= 2
            days += 1
    print(days)
