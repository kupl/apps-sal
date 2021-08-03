import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

mod = 10**9 + 7

SUM = sum(A)
r = M - SUM
S = r + SUM + N

F = 1
for i in range(1, S - r + 1):
    F = F * i % mod


if M < SUM:
    print((0))
else:
    ANS = 1
    y = 1
    for i in range(S - r):
        ANS = ANS * S % mod
        S -= 1
    ANS = ANS * pow(F, mod - 2, mod) % mod

    print(ANS)
