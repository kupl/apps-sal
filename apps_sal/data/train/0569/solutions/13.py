t = int(input())
for i in range(t):
    n = int(input())
    x = int(((8 * (n + 1) + 1) ** 0.5 - 1) / 2)
    d = (8 * (n + 1) + 1) ** 0.5
    if d - int(d) == 0:
        print(x - 1)
    else:
        f = x * (x + 1) // 2
        c = n - f
        print(c)
