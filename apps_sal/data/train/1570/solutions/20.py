import sys
T = int(input())
for t in range(T):
    N = int(input())
    res = N * (N + 1) * (2 * N + 1) / 6
    print(int(res))
