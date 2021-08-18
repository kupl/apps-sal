import random
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    REST = [-1] * n
    MIN = 1 << 60
    RESTMAX = 0

    for i in range(n):
        MIN = min(MIN, A[i])

        if A[i] - MIN < RESTMAX:
            MIN = max(0, A[i] - RESTMAX)
            REST[i] = A[i] - MIN
            RESTMAX = max(RESTMAX, REST[i])

        else:
            REST[i] = A[i] - MIN
            RESTMAX = max(RESTMAX, REST[i])

    for i in range(1, n):
        if REST[i - 1] == 0:
            continue
        if REST[i - 1] > REST[i]:
            print("NO")
            break
    else:
        print("YES")
