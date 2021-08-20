for _ in range(int(input())):
    x = [int(w) for w in input().split()]
    ind = x.index(-1)
    x = x[:ind]
    ctr = 0
    (a, b) = (0, 0)
    for i in range(len(x)):
        if x[i] > 30:
            ctr += 1
        if x[i] % 2 == 0:
            a += (i + 1) * x[i]
            b += i + 1
    ans = a / b
    print(ctr, '%.2f' % ans)
