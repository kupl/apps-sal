def I(): return list(map(int, input().split()))


t = I()[0]
while(t):
    t -= 1
    n = I()[0]
    arr = I()
    d = {}
    for i in arr:
        d[i] = 0
    for i in arr:
        d[i] += 1
    extra = 0
    for i in list(d.keys()):
        if(d[i] > 1):
            extra += (d[i] - 1)
    if(extra % 2):
        extra += 1
    print(n - extra)
