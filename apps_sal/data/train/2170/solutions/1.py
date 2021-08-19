from heapq import heappop as hpp, heappush as hp
import sys
readline = sys.stdin.readline
INF = 10 ** 9 + 7


def calc(A, x):
    if A < x:
        return INF
    (d, r) = divmod(A, x)
    return d * d * x + (2 * d + 1) * r


(N, K) = list(map(int, readline().split()))
A = list(map(int, readline().split()))
Q = [(-calc(a, 1) + calc(a, 2), a, 1) for a in A]
Q.sort()
for _ in range(K - N):
    (dif, a, x) = hpp(Q)
    hp(Q, (-calc(a, x + 1) + calc(a, x + 2), a, x + 1))
ans = 0
for (_, a, x) in Q:
    ans += calc(a, x)
print(ans)
