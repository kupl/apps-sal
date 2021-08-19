for _ in range(int(input())):
    count = 0
    l = list(map(int, input().split(' ')))
    s = 0
    d = 0
    i = 1
    for x in l:
        if x > 30:
            count += 1
        if x % 2 == 0:
            s += i * x
            d += i
        i += 1
    print(count, end=' ')
    print('%.2f' % (s / d))
