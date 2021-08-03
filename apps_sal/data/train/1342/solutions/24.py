for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    days = 0
    for i in a:
        if i <= m:
            m = max(2 * i, m)
            days += 1
        else:
            t = m
            days += 1
            while t < i:
                t *= 2
                days += 1
            m = 2 * t
    print(days)
