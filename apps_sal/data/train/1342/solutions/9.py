for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    i = 0
    days = 0
    while(i < n and 2 * l[i] <= x):
        i += 1
        days += 1
    while(i < n):
        days += 1
        if(l[i] > x and 2 * (l[i] - x) >= l[i]):
            x = 2 * x
            continue
        if(l[i] <= x):
            x = l[i]
            i += 1
        x = 2 * x
    print(days)
