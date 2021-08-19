for _ in range(int(input())):
    (R, G, B, M) = map(int, input().split())
    l = []
    r = list(map(int, input().split()))
    rm = max(r)
    g = list(map(int, input().split()))
    gm = max(g)
    b = list(map(int, input().split()))
    bm = max(b)
    l = [rm, gm, bm]
    l.sort()
    for i in range(M):
        l[-1] //= 2
        l.sort()
    print(l[-1])
