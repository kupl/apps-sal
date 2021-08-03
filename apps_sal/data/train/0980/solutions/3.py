
import sys

for i in range(int(input())):
    # line =
    [N, B, M] = list(map(int, input().split()))
    t = 0
    while N > 0:
        if N % 2 == 0:
            t += (N / 2) * M
            N = N / 2
        else:
            t += ((N + 1) / 2) * M
            N = (N - 1) / 2
        M = M * 2
        if N > 0:
            t += B
    print(t)
