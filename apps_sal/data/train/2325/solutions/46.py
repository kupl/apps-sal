
from itertools import accumulate

*S, = map(lambda x: 1 if x == 'A' else 2, input())
*T, = map(lambda x: 1 if x == 'A' else 2, input())

acc_s = (0,) + tuple(accumulate(S))
acc_t = (0,) + tuple(accumulate(T))

ans = []
Q = int(input())
for _ in range(Q):
    sl, sr, tl, tr = map(int, input().split())
    sl -= 1
    tl -= 1
    diff = (acc_t[tr] - acc_t[tl]) - (acc_s[sr] - acc_s[sl])
    ans.append('YES' if diff % 3 == 0 else 'NO')

print(*ans, sep='\n')
