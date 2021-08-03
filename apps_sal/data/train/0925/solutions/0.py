import math


def comb(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    m = 0
    ans = 0.0
    for i in range(0, n):
        if (arr[i] == -1):
            m = m + 1
    for i in range(0, m):
        ans = ans + ((m - i) * comb(m - 1, m - 1 - i))
    ans = ans / pow(2, m - 1)
    print('{0:.7f}'.format(ans))
