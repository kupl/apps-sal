import sys
from itertools import accumulate
readline = sys.stdin.readline

S = [1 if s == 'A' else 2 for s in readline().strip()]
T = [1 if s == 'A' else 2 for s in readline().strip()]
AS = [0] + list(accumulate(S))
AT = [0] + list(accumulate(T))
Q = int(readline())
Ans = [None] * Q

for qu in range(Q):
    a, b, c, d = map(int, readline().split())
    if (AS[b] - AS[a - 1]) % 3 != (AT[d] - AT[c - 1]) % 3:
        Ans[qu] = 'NO'
    else:
        Ans[qu] = 'YES'

print('\n'.join(map(str, Ans)))
