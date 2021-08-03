for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    for _ in range(1, n, 2):
        a[_], a[_ - 1] = a[_ - 1], a[_]
    for _ in range(n):
        a[_] += (a[_] % 3)
    # a=a[::-1]
    # a.sort()
    # if x>a[-1]:
    #     print(-1)
    #     continue
    l, h = -1, 9999999999
    for _ in range(n):
        # if a[_]>=x:
        #     if _==n-1:
        #         print(-1)
        #         break
        #     elif _==0:
        #         print(-1)
        #         break
        #     else:
        #         print(a[_-1],a[_])
        #         break
        if a[_] > l and a[_] < x:
            l = a[_]
        if a[_] < h and a[_] > x:
            h = a[_]
    print(l, end=" ")
    if h == 9999999999:
        print(-1)
    else:
        print(h)
