try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        x = int(input())
        b = list(map(lambda x: x + x % 3, a))
        b.sort()
        c1 = 0
        for lar in b:
            if lar > x:
                large = lar
                c1 = 1
                break
        if c1 == 0:
            large = -1
        b.sort(reverse=True)
        c2 = 0
        for sma in b:
            if sma < x:
                small = sma
                c2 = 1
                break
        if c2 == 0:
            small = -1
        print(small, large)
except:
    pass
