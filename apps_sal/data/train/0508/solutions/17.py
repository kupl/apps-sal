from bisect import bisect_left
from operator import itemgetter


def main():
    (N, Q, *STXD) = list(map(int, open(0).read().split()))
    D = STXD[3 * N:]
    ans = [-1] * Q
    road = [-1] * Q
    for (s, t, x) in sorted(zip(*[iter(STXD[:3 * N])] * 3), key=itemgetter(2)):
        (l, r) = (bisect_left(D, s - x), bisect_left(D, t - x))
        while l < r:
            if road[l] == -1:
                ans[l] = x
                road[l] = r
                l += 1
            else:
                l = road[l]
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
