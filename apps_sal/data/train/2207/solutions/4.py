while 1:
    try:
        n = int(input())
        (a, b, c) = ([0 for j in range(n)], [0 for j in range(n)], [0 for j in range(n)])
        (sum1, sum2) = (0, 0)
        for i in range(0, n):
            (a[i], b[i], c[i]) = list(map(int, input().split()))
            if a[i] == 1:
                sum1 += b[i]
            else:
                sum2 += b[i]
        (count1, count2) = (a.count(1), a.count(2))
        (t1, t2) = (10 * count1, 10 * count2)
        if sum1 / t1 >= 0.5:
            print('LIVE')
        else:
            print('DEAD')
        if sum2 / t2 >= 0.5:
            print('LIVE')
        else:
            print('DEAD')
    except EOFError:
        break
