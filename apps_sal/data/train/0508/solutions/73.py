import sys
input = sys.stdin.readline
INF = 1<<31
from bisect import bisect_left

def main():
    N,Q = map(int,input().split())
    roadwork = [tuple(map(int,input().split())) for _ in range(N)]
    roadwork.sort(key = lambda x:x[2])
    D = [int(input()) for _ in range(Q)]
    ans = [-1] * Q
    skip = [-1] * Q
    for s,t,x in roadwork:
        L = bisect_left(D,s - x)
        R = bisect_left(D,t - x)
        while L < R:
            if skip[L] == -1:
                ans[L] = x
                skip[L] = R
                L += 1
            else:
                L = skip[L]
    print('\n'.join(map(str,ans)))
def __starting_point():
    main()
__starting_point()
