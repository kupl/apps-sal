for _ in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    d = {}
    for i in m:
        try:
            d[i]
        except:
            d[i] = 1
        else:
            d[i] += 1
    mam, mim = max(m), min(m)
    pc = list(d.items())
    if len(pc) == 2 and mam == mim + 1:
        if d[mam] + d[mim] == n and mim == d[mim] - 1:
            ans = d[mam]
        else:
            ans = -1
    elif len(pc) == 1:
        if mam == n - 1:
            ans = 0
        elif mam == 0:
            ans = n
        else:
            ans = -1
    else:
        ans = -1
    print(ans)
