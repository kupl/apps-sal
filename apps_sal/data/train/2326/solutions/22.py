def main():
    import sys
    import bisect
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] + sorted(a)
    res = [0] * n
    d = dict()
    for i in range(n):
        if not a[i] in d:
            d[a[i]] = i
    p = n
    while p > 0:
        k = bisect.bisect_left(b, b[p])
        res[d[b[k]]] += (n + 1 - k) * (b[k] - b[k - 1])
        if k - 1 >= 1:
            d[b[k - 1]] = min(d[b[k]], d[b[k - 1]])
        p = k - 1
    for e in res:
        print(e)


def __starting_point():
    main()


__starting_point()
