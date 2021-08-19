def main():
    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    from collections import defaultdict as dd, deque

    def data():
        return sys.stdin.readline().strip()

    def mdata():
        return list(map(int, data().split()))
    out = sys.stdout.write
    INF = int(1000000000.0)
    mod = int(1000000000.0) + 7
    for t in range(int(data())):
        n = int(data())
        A = mdata()
        d = dd(list)
        for i in range(n):
            d[A[i]].append(i)
        l = sorted(d.keys())
        cnt = 1
        ind = d[l[0]][0]
        for i in range(1, len(l)):
            k = bl(d[l[i]], ind)
            if k == len(d[l[i]]):
                cnt += 1
                ind = d[l[i]][0]
            else:
                ind = d[l[i]][k]
        print(cnt)


def __starting_point():
    main()


__starting_point()
