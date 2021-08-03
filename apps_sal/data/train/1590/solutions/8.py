try:
    for _ in range(int(input())):
        g, t, w = map(int, input().rstrip().split())
        m = max(g, t, w)
        total = g + t + w - m
        if m - total < 2:
            print('Yes')
        else:
            print('No')
except:
    pass
