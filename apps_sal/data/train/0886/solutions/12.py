import bisect
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    for i in range(n):
        mod = lst[i] % 3
        lst[i] = lst[i] + mod
    lst = sorted(lst)
    id = bisect.bisect(lst, m)
    if id == 0:
        if lst[0] > m:
            g = lst[0]
        else:
            g = lst[1]
        s = -1
    elif id == n:
        if lst[n - 1] < m:
            s = lst[n - 1]
        else:
            s = lst[n - 2]
        g = -1
    else:
        s = lst[id - 1]
        if s == m:
            if id - 2 < 0:
                s = -1
            else:
                s = lst[id - 2]
        g = lst[id]
        if g == m:
            if id + 1 > n - 1:
                g = -1
            else:
                g = lst[id + 1]
    print(s, g)
