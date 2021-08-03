T = int(input())


def nasu(a, b, c):
    mi = min(a, b, c)
    ma = max(a, b, c)
    f = False
    if mi >= 0:
        f = True
        t = (ma - 1) * 2
        if a + b + c == ma * 2 + mi:
            t += 1
        return t, f
    else:
        t = -mi * 2 - 1
        if a + b + c == mi * 2 + ma:
            t += 1
        return t, f


def main():
    ax, ay, bx, by, cx, cy = list(map(int, input().split()))
    ans = 0
    x, xf = nasu(ax, bx, cx)
    y, yf = nasu(ay, by, cy)
    ans += max(x, y)
    if xf and yf and x == y and x >= 2:
        ans += 1
    if not xf and not yf and x == y and x >= 1:
        ans += 1
    print(ans)


for i in range(T):
    main()
