for _ in range(int(input())):
    a, d, k, n, inc = list(map(int, input().split()))
    sum1 = a
    for i in range(0, n):
        if i == 0:
            pass
        else:
            if i % k == 0:
                d += inc
            sum1 += d

    print(sum1)
