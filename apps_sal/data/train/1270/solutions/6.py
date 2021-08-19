for _ in range(int(input())):
    (n, k) = map(int, input().split())
    h = list(map(int, input().split()))
    sum = 0
    h.sort()
    h1 = set()
    h1.add(h[n - 1])
    summ = h[n - 1]
    z = -1
    for i in range(n - 2, -1, -1):
        h2 = set()
        summ = summ + h[i]
        i1 = iter(h1)
        while True:
            try:
                p = int(next(i1))
            except StopIteration:
                break
            h2.add(p)
            h2.add(h[i])
            h2.add(p + h[i])
            if p + h[i] >= k and summ - p - h[i] >= k:
                z = n - i
                break
            if h[i] >= k and summ - h[i] >= k:
                z = n - i
                break
        if z != -1:
            break
        h1 = h2
    print(z)
