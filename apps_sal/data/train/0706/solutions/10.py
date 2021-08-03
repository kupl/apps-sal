for i in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ro = 0
    s = 0
    f = 1
    for i in range(n):
        if l[i] > k:
            print(-1)
            f = 0
            break
        s += l[i]
        if s > k:
            s = l[i]
            ro += 1
    if s and f:
        print(ro + 1)
    elif f:
        print(ro)
