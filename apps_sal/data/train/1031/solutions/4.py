t = int(input())
for test in range(t):
    h, s = list(map(int, input().split()))
    if h**2 >= 4 * s:
        x = (h**2 + 4 * s)**0.5
        y = (h**2 - 4 * s)**0.5
        res = list(map(float, sorted([h, (x + y) / 2, (x - y) / 2])))
        print("%.5f %.5f %.5f" % (res[0], res[1], res[2]))
    else:
        print(-1)
