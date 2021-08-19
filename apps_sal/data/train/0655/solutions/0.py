def __starting_point():
    t = int(input())
    for _ in range(t):
        (n, k, v) = map(int, input().split())
        li = list(map(int, input().split()))
        sumn = 0
        for i in range(n):
            sumn = sumn + li[i]
        sumk = v * (n + k) - sumn
        e = int(sumk / k)
        r = sumk % k
        if e <= 0:
            print(-1)
        elif r != 0:
            print(-1)
        else:
            print(e)


__starting_point()
