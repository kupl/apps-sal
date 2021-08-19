for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l.sort()
    days = 0
    for target in l:
        while x < target:
            x <<= 1
            days += 1
        x = max(x, target << 1)
        days += 1
    print(days)
