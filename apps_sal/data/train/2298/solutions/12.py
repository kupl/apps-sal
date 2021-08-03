def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n, t = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    d = collections.defaultdict(list)
    min_b = 10 ** 9
    max_p = 0
    for v in a:
        p = v - min_b
        max_p = max(max_p, p)
        d[p] += [min_b]
        min_b = min(min_b, v)
    print((len(d[max_p])))


def __starting_point():
    slove()


__starting_point()
