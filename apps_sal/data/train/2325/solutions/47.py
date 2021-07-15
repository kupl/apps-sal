# https://atcoder.jp/contests/arc071/submissions/6325840

from itertools import accumulate

S = tuple(map(lambda x: 1 if x == 'A' else 2, input()))
T = tuple(map(lambda x: 1 if x == 'A' else 2, input()))
# A=1,B=2


acc_s = (0,) + tuple(accumulate(S))
acc_t = (0,) + tuple(accumulate(T))

ans = []
Q = int(input())
for _ in range(Q):
    sl, sr, tl, tr = map(int, input().split())
    diff = (acc_t[tr] - acc_t[tl - 1]) - (acc_s[sr] - acc_s[sl - 1])
    # 添え字-1は変数再代入しない方が20ms速い
    ans.append('YES' if diff % 3 == 0 else 'NO')

print(*ans, sep='\n')
# 逐次printだと1000ms
# 一括だと500ms

