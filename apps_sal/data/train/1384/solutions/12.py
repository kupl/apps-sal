#!/usr/bin/env python3
def solve(n, k, s):
    l = [None] * (n + 1)
    l[0] = 0
    for i in range(n):
        if int(s[i]):
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = 0

    r = [None] * (n + 1)
    r[n] = 0
    for i in reversed(list(range(n))):
        if int(s[i]):
            r[i] = r[i + 1] + 1
        else:
            r[i] = 0

    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, l[i] + k + r[i + k])
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        s = input()
        print(solve(n, k, s))


def __starting_point():
    main()


__starting_point()
