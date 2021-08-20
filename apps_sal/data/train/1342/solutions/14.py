for _ in range(int(input())):
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] >= x // 2:
            break
    p = i
    while 1:
        if a[i] <= x:
            count += 1
            x = 2 * a[i]
        else:
            while a[i] > x:
                x = 2 * x
                count += 1
            x = 2 * a[i]
            count += 1
        i += 1
        if i == n:
            break
    print(count + p)
