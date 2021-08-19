for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = 1
    for j in range(1, n):
        if j - 5 < 0:
            mi = min(a[0:j])
            # print(a[0:j])
            if mi > a[j]:
                g = g + 1
        else:
            mi = min(a[j - 5:j])
            # print(a[j-5:j])
            if mi > a[j]:
                g = g + 1
    print(g)
