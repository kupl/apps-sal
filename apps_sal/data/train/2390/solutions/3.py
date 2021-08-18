from collections import Counter
import sys
input = sys.stdin.readline

Q = int(input())
for testcase in range(Q):
    n = int(input())
    A = Counter((list(map(int, input().split()))))
    S = sorted(list(A.values()), reverse=True)

    NOW = 10**10

    ANS = 0
    for s in S:
        M = min(NOW, s)
        ANS += M
        NOW = M - 1

        if NOW == 0:
            break

    print(ANS)
