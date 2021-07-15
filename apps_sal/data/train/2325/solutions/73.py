# https://atcoder.jp/contests/arc071/submissions/6325840

from itertools import accumulate

convert = {'A': 1, 'B': 2}
S = tuple(convert[x] for x in input())
T = tuple(convert[x] for x in input())
# 最速:   convert
# 次点:   *A, = map()
# 最下位: A = tuple(map())

acc_s = (0,) + tuple(accumulate(S))
acc_t = (0,) + tuple(accumulate(T))

ans = []
Q = int(input())
for _ in range(Q):
    sl, sr, tl, tr = map(int, input().split())
    # 添え字-1は変数再代入しない方が20ms速い
    ans.append('YES' if ((acc_t[tr] - acc_t[tl - 1]) - (acc_s[sr] - acc_s[sl - 1])) % 3 == 0 else 'NO')

print(*ans, sep='\n')
# 逐次printだと1000ms
# 一括だと500ms

