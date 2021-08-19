for t in range(int(input())):
    (n, x) = list(map(int, input().split()))
    numberlist = list(map(int, input().split()))
    numberlist.sort()
    count = 0
    for f in numberlist:
        if f >= x:
            count = count + 1
    if count > 0:
        print('YES')
    else:
        print('NO')
