def abc(i, n, w, x, c):
    if c == n:
        return x == w
    ans = 0
    for j in range(10):
        ans += abc(j, n, w, x + j - i, c + 1)
    return ans


e = 10**9 + 7
t = int(input())
for _ in range(t):
    n, w = list(map(int, input().split()))
    ans = 0
    for i in range(1, 10):
        pass
    if n == 1:
        if w == 0:
            print(9)
        else:
            print(0)
    else:
        if w >= 9:
            print(0)
        elif w > 0:
            x = ((9 - w) * pow(10, n - 2, e)) % e
            print(x)
        elif w <= -10:
            print(0)
        elif w == 0:
            print((9 * pow(10, n - 2, e)) % e)
        else:
            c = -w
            x = ((10 - c) * pow(10, n - 2, e)) % e
            print(x)


0
