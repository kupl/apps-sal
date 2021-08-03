for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    m = a[0]
    v = 0
    for i in a:
        v = max(v, m - i)
        m = max(m, i)
    if v == 0:
        print(0)
    else:
        p = 1
        c = 0
        while p <= v:
            p *= 2
            c += 1
        print(c)
