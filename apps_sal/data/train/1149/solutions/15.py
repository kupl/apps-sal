def solve():
    s = input()
    n = len(s)
    c = 1
    for i in range(((n - 1) // 2) + 1):
        if s[i] == '?' and s[n - i - 1] == "?":
            c = (c * 26) % 10000009
        elif s[i] == '?' or s[n - i - 1] == "?":
            c = c * 1
        elif s[i] != s[n - i - 1]:
            c = 0
            break

    print(c)


def __starting_point():
    t = int(input())
    while t > 0:
        solve()
        t = t - 1


__starting_point()
