"""
            1                   n == 1 or m == 1
f(n,m) =     f(n,n-1)+1          m >= n
            f(n,m-1)+f(n-m,m)   m < n
"""


def partitions(n):
    d = {}
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x == 1 or y == 1:
                d[x, y] = 1
            elif x <= y:
                d[x, y] = d[x, x - 1] + 1
            else:
                d[x, y] = d[x, y - 1] + d[x - y, y]
    return d[n, n]
