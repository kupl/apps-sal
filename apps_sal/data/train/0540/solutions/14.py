for _ in range(int(input())):
    (n, m) = [int(x) for x in input().split()]
    ls = [int(X) for X in input().split()]
    x = ls.count(m)
    ls2 = list(set(ls))
    if len(ls2) <= m - 2:
        print(-1)
    elif ls2[m - 2] != m - 1:
        print(-1)
    else:
        print(n - x)
