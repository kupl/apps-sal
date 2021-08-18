
from itertools import accumulate

S = tuple(map(lambda x: 1 if x == 'A' else 2, input()))
T = tuple(map(lambda x: 1 if x == 'A' else 2, input()))


acc_s = (0,) + tuple(accumulate(S))
acc_t = (0,) + tuple(accumulate(T))

ans = []
Q = int(input())
for _ in range(Q):
    sl, sr, tl, tr = map(int, input().split())
    diff = (acc_t[tr] - acc_t[tl - 1]) - (acc_s[sr] - acc_s[sl - 1])
    ans.append('YES' if diff % 3 == 0 else 'NO')

print(*ans, sep='\n')
