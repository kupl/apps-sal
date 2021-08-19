import sys
from collections import Counter
readline = sys.stdin.readline
(N, T) = map(int, readline().split())
A = list(map(int, readline().split()))
Amax = [None] * N
Amax[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    Amax[i] = max(Amax[i + 1], A[i])
B = [am - a for (a, am) in zip(A, Amax)]
print(Counter(B)[max(B)])
