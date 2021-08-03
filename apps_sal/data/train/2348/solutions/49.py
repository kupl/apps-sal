from bisect import bisect_left

INF = float('inf')


def check(a, b):
    ng, ok = -1, N + 1
    while(ok - ng > 1):
        mid = (ng + ok) // 2
        now = a
        bit = 0
        x = mid
        while(x):
            if x & 1:
                now = A[now][bit]
            bit += 1
            x >>= 1
        if b <= now:
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
x = list(map(int, input().split()))

K = N.bit_length() - 1

L = int(input())

A = [[INF] * (K + 1) for _ in range(N)]

for i in range(N):
    b = bisect_left(x, x[i] + L + 1)
    A[i][0] = b - 1

for k in range(K):
    for i in range(N):
        A[i][k + 1] = A[A[i][k]][k]

Q = int(input())
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    if a > b:
        a, b = b, a
    print(check(a, b))
