for _ in range(int(input())):
    n, u, d = map(int, input().split())
    a = list(map(int, input().split()))
    x = 1
    count = 1
    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            if a[i] + u >= a[i + 1]:
                count += 1
            elif a[i] + u < a[i + 1]:
                break
        else:
            if a[i] - d <= a[i + 1]:
                count += 1
            elif x == 1:
                count += 1
                x = 0
            else:
                break
    print(count)
