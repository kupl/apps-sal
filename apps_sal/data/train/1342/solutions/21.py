for i in range(int(input())):
    n, x = map(int, input().split())
    cnt = list(map(int, input().split()))
    cnt.sort()
    day = 0
    j = 0
    while j < n:
        day += 1
        if cnt[j] - x <= 0:
            x = max(x, 2 * cnt[j])
            j += 1
        else:
            x = 2 * x

    print(day)
