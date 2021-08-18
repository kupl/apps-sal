
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    ays = list(map(int, input().split()))

    gt = 0
    gtp = -1
    mseg = 0
    seg = 0
    for ax, a in enumerate(ays):
        if a <= k:
            seg += 1
        elif gt == 0:
            seg += 1
            gt = a
            gtp = ax
        elif a == gt:
            seg += 1
            gtp = ax
        else:
            if seg > mseg:
                mseg = seg
            gt = a
            seg = ax - gtp
            gtp = ax

    if seg > mseg:
        mseg = seg
    print(mseg)
