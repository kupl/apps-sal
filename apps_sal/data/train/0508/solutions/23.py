import sys
from heapq import heappush, heappop
from operator import itemgetter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, Q = map(int, readline().split())
    work = [0] * N
    for i in range(N):
        s, t, x = map(int, readline().split())
        work[i] = (x, s - x, t - x)
    query = list(map(int, read().split()))

    work.sort(key=itemgetter(1), reverse=True)
    hq = []
    ans = [0] * Q

    for i, d in enumerate(query):
        while work and work[-1][1] <= d:
            heappush(hq, work[-1])
            work.pop()
        while hq and hq[0][2] <= d:
            heappop(hq)
        if not hq:
            ans[i] = -1
        else:
            ans[i] = hq[0][0]

    print(*ans, sep='\n')
    return


def __starting_point():
    main()


__starting_point()
