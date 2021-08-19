for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    ays = list(map(int, input().split()))
    gt = k
    gtp = -1
    mseg = 0
    seg = 0
    for (ax, a) in enumerate(ays):
        if a <= k:
            seg += 1
        elif a == gt:
            seg += 1
            gtp = ax
        else:
            if seg > mseg:
                mseg = seg
            gt = a
            seg = ax - gtp
            gtp = ax
    if gt == k:
        mseg = 0
    elif seg > mseg:
        mseg = seg
    print(mseg)
