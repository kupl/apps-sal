import sys
import statistics
from statistics import mode
readline = sys.stdin.readline
try:
    INF = 10 ** 18 + 3
    (N, M, K) = map(int, readline().split())
    Points = [tuple(map(int, readline().split())) for _ in range(K)]
    ABC = [(p[1], p[3], abs(p[0] - p[2])) for p in Points]
    ans = INF
    l = []
    ans = INF
    for m in range(1, M + 1):
        res = 0
        for (a, b, c) in ABC:
            res += min(2 * abs(a - m) + 2 * abs(b - m) + c, 2 * abs(a - b) + 2 * c)
        ans = min(ans, res)
    print(ans)
except:
    pass
