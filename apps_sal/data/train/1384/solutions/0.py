for _ in range(int(input())):
    (n, k) = map(int, input().split())
    l = [*map(int, input())]
    count = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if l[i] == 1:
            count[i] = count[i + 1] + 1
    (x, y) = (0, 0)
    for i in range(n):
        if l[i] == 1:
            x += 1
        else:
            try:
                y = max(y, x + k + count[i + k])
            except:
                y = max(y, x + min(k, n - i))
            x = 0
        y = max(y, x)
    print(y)
