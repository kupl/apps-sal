for t in range(int(input())):
    (n, d) = [int(x) for x in input().rstrip().split()]
    a = [int(x) for x in input().rstrip().split()]
    count = 0
    day = 0
    for i in range(0, n):
        if a[i] <= 9:
            count += 1
        elif a[i] >= 80:
            count += 1
        else:
            pass
    n = n - count
    while count != 0:
        if count >= d:
            count -= d
            day += 1
        else:
            day += 1
            break
    while n != 0:
        if n >= d:
            n -= d
            day += 1
        else:
            n = 0
            day += 1
            break
    print(day)
