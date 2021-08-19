from math import gcd
__author__ = 'Prateek'


def test():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    n = len(a)
    if len(a) == 1:
        print(2 * a[0])
        return
    g1 = [0 for i in range(n)]
    g2 = [0 for i in range(n)]
    g1[0] = a[0]
    g2[n - 1] = a[n - 1]
    for i in range(1, n):
        g1[i] = gcd(g1[i - 1], a[i])
    for i in range(n - 2, -1, -1):
        g2[i] = gcd(g2[i + 1], a[i])
    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, g2[i + 1] + a[i])
        elif i == n - 1:
            ans = max(ans, g1[i - 1] + a[i])
        else:
            ans = max(ans, gcd(g1[i - 1], g2[i + 1]) + a[i])
    print(ans)


if __author__ == 'Prateek':
    t = int(input())
    for _ in range(t):
        test()
