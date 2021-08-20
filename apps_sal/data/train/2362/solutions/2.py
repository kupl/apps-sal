y = 10 ** 5
T = int(input())
for _ in range(T):
    x = [-y, -y, y, y]
    n = int(input())
    for _ in range(n):
        a = list(map(int, input().split()))
        if not a[2]:
            x[0] = max(x[0], a[0])
        if not a[3]:
            x[3] = min(x[3], a[1])
        if not a[4]:
            x[2] = min(x[2], a[0])
        if not a[5]:
            x[1] = max(x[1], a[1])
    if x[0] <= x[2] and x[1] <= x[3]:
        print(1, x[0], x[1])
    else:
        print(0)
