for _ in range(int(input())):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x, z = 0, 0
    if b[0] == 1:
        y = 1
    else:
        y = 2
    c = True
    for i in range(1, n):
        if y != b[i]:
            if (a[i] - x <= d and z != 0) or a[i] - a[i - 1] == 1:
                c = False
                print(a[i])
                break
            if (z == 0):
                z = 1
                x = a[i - 1] + 1
            else:
                x = max(a[i - 1] + 1, x + d)
            y = b[i]
    if c:
        print(k)
