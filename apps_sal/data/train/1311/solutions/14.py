for i in range(int(input())):
    n, k = list(map(int, input().split()))
    l = []
    pos = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            l.append(-1 * i)
        else:
            l.append(i)
            pos += 1
    if pos < k:
        g = k - pos
        c = 0
        for i in range(n - 1, -1, -1):
            if l[i] < 0:
                l[i] = -1 * l[i]
                c += 1
            if c == g:
                break
    if pos > k:
        g = pos - k
        c = 0
        for i in range(n - 1, -1, -1):
            if l[i] > 0:
                l[i] = -1 * l[i]
                c += 1
            if c == g:
                break
    print(*l)
