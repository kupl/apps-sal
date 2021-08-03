for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = False
    d = 0
    for i in range(1, n - 3):
        if a[i] - a[i - 1] != a[i + 1] - a[i]:
            d = a[i + 3] - a[i + 2]
            a[i + 1] = a[i + 2] - d
            a[i] = a[i + 1] - d
            a[i - 1] = a[i] - d
            f = True
            break

    if (not f):
        if (a[n - 1] - a[n - 4]) / 3 == (a[n - 1] - a[n - 2]):
            d = a[n - 1] - a[n - 2]
            a[n - 3] = a[n - 2] - d
        elif (a[n - 1] - a[n - 4]) / 3 == (a[n - 1] - a[n - 3]) / 2:
            d = a[n - 3] - a[n - 4]
            a[n - 2] = a[n - 3] + d
        elif a[n - 1] - a[n - 2] == a[n - 2] - a[n - 3]:
            d = a[n - 1] - a[n - 2]
            a[n - 4] = a[n - 3] - d
        else:
            d = a[n - 3] - a[n - 4]
            a[n - 1] = a[n - 2] + d

    [print(x, end=" ") for x in a]
    print()
