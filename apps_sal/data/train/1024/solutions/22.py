try:
    t = int(input())
    required = 0
    avaliable = 0
    for i in range(t):
        s, n, k, r = list(map(int, input().strip().split(' ')))
        total = k
        for i in range(n - 1):
            total += k * r
            k = k * r
        if total > s:
            print("IMPOSSIBLE", total - s)
            required += total - s
        else:
            print("POSSIBLE", s - total)
            avaliable += s - total
    if required <= avaliable:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
except:
    pass
