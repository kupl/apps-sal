import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    MINA = min(A)
    MINB = min(B)

    ANS = 0

    for i in range(n):
        a = A[i]
        b = B[i]

        aa = a - MINA
        bb = b - MINB

        ANS += max(aa, bb)

    print(ANS)
