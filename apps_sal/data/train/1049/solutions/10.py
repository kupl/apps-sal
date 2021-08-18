for u in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    m = 0
    s = set(l)
    r = len(s)
    for i in range(n - k + 1):
        c = 0
        d = set()
        for j in range(i, i + k):
            c += l[j]
            d.add(l[j])
        if(len(d) == r):
            m = max(m, c)
    print(m)
