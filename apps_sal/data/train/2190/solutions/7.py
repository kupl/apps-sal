def main():
    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import math
    from collections import defaultdict as dd, deque

    def data():
        return sys.stdin.readline().strip()

    def mdata():
        return list(map(int, data().split()))
    out = sys.stdout.write
    INF = float('INF')
    mod = int(1000000000.0) + 7
    n = int(data())
    l = mdata()
    cnt = 0
    m = 0
    max1 = 0
    X = []
    for i in l[::-1]:
        while len(X) and X[-1][0] < i:
            m = max(m + 1, X[-1][1])
            X.pop()
        X.append([i, m])
        if m > max1:
            max1 = m
        m = 0
    print(max1)


def __starting_point():
    main()


__starting_point()
