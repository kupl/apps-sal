
import bisect
T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    aa = sorted([int(input(), 2) for _ in range(N)])

    K = 1 << M

    ans = 0

    for k in reversed(list(range(M))):
        tmp = ans + (1 << k)
        La = bisect.bisect_left(aa, tmp)
        Ra = N - La

        L = tmp - La
        R = (K - tmp) - Ra

        if L < R:
            ans = tmp
        else:
            continue

    print(f"{ans:0{M}b}")

