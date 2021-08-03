mod = 10000009


def solve():
    s = input()
    n = len(s)
    c, k = 1, 0
    for i in range(((len(s) - 1) // 2) + 1):
        if s[i] == '?' and s[n - i - 1] == '?':
            c = (c * 26) % 10000009
        elif s[i] == '?' or s[n - i - 1] == '?':
            pass
        elif s[i] != s[n - i - 1]:
            k = 1
            break
    if k == 1:
        print(0)
    else:
        print(c)


def __starting_point():
    t = int(input())
    while t != 0:
        solve()
        t -= 1


__starting_point()
