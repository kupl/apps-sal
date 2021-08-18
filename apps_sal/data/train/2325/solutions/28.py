
from itertools import accumulate

convert = {'A': 1, 'B': 2}
S = tuple(convert[x] for x in input())
T = tuple(convert[x] for x in input())

acc_s = (0,) + tuple(accumulate(S))
acc_t = (0,) + tuple(accumulate(T))

ans = []
Q = int(input())
for _ in range(Q):
    sl, sr, tl, tr = map(int, input().split())
    ans.append('YES' if (acc_t[tr] - acc_t[tl - 1]) % 3 == (acc_s[sr] - acc_s[sl - 1]) % 3 else 'NO')

print(*ans, sep='\n')
