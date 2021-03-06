import decimal
import sys


def C(N, K):
    if K > N:
        return 0
    if N - K < K:
        K = N - K
    res = 1
    i = 1
    while i <= K:
        res = res * (N - K + i)
        res = int(res / i)
        i = i + 1
    return res


T = int(sys.stdin.readline())
for t in range(T):
    (N, K) = list(map(int, sys.stdin.readline().split()))
    print(C(N, K))
