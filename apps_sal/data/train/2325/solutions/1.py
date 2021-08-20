from itertools import accumulate
import sys
S = input()
T = input()
ns = len(S)
nt = len(T)
SA = [0] * (ns + 1)
SB = [0] * (ns + 1)
TA = [0] * (nt + 1)
TB = [0] * (nt + 1)
for (i, s) in enumerate(S, 1):
    if s == 'A':
        SA[i] = 1
    else:
        SB[i] = 1
for (i, t) in enumerate(T, 1):
    if t == 'A':
        TA[i] = 1
    else:
        TB[i] = 1
SA = list(accumulate(SA))
SB = list(accumulate(SB))
TA = list(accumulate(TA))
TB = list(accumulate(TB))
q = int(input())
for _ in range(q):
    (a, b, c, d) = map(int, input().split())
    sa = SA[b] - SA[a - 1]
    sb = SB[b] - SB[a - 1]
    ta = TA[d] - TA[c - 1]
    tb = TB[d] - TB[c - 1]
    sb += 2 * sa
    tb += 2 * ta
    if abs(sb - tb) % 3 == 0:
        print('YES')
    else:
        print('NO')
