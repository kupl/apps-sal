import sys
readline = sys.stdin.readline

T = int(readline())
INF = 10**9 + 7
Ans = [None] * T
for qu in range(T):
    N = int(readline())
    A = list(map(int, readline().split()))

    res = INF
    rem = 0
    for i in range(N):
        res = max(0, min(res, A[i] - rem))
        A[i] -= res
        rem = A[i]
    Ans[qu] = 'YES' if all(a2 - a1 >= 0 for a1, a2 in zip(A, A[1:])) else 'NO'

print('\n'.join(map(str, Ans)))
