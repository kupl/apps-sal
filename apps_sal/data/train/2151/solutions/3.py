def __starting_point():
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    i = n // 2
    median = a[i]
    result = 0
    if median > s:
        for j in range(i + 1):
            result += max(0, a[j] - s)
    elif median < s:
        for j in range(i, n):
            result += max(0, s - a[j])
    print(result)


__starting_point()
