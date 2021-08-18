from sys import stdin, stdout
import sys
from bisect import bisect_left, bisect_right
import heapq
sys.setrecursionlimit(2 * (10**5))


n, m = stdin.readline().strip().split(' ')
n, m = int(n), int(m)

costarr = []
for i in range(n):
    costarr.append(list(map(int, stdin.readline().strip().split(' '))))


dp_tl_br = [[0 for i in range(m)] for j in range(n)]
dp_br_tl = [[0 for i in range(m)] for j in range(n)]
dp_bl_tr = [[0 for i in range(m)] for j in range(n)]
dp_tr_bl = [[0 for i in range(m)] for j in range(n)]

dp_tl_br[0][0] = costarr[0][0]
for i in range(1, m):
    dp_tl_br[0][i] = dp_tl_br[0][i - 1] + costarr[0][i]
for i in range(1, n):
    dp_tl_br[i][0] = dp_tl_br[i - 1][0] + costarr[i][0]
for i in range(1, n):
    for j in range(1, m):
        dp_tl_br[i][j] = max(dp_tl_br[i][j - 1], dp_tl_br[i - 1][j]) + costarr[i][j]


dp_br_tl[n - 1][m - 1] = costarr[n - 1][m - 1]
for i in range(m - 2, -1, -1):
    dp_br_tl[n - 1][i] = dp_br_tl[n - 1][i + 1] + costarr[n - 1][i]
for i in range(n - 2, -1, -1):
    dp_br_tl[i][m - 1] = dp_br_tl[i + 1][m - 1] + costarr[i][m - 1]
for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        dp_br_tl[i][j] = max(dp_br_tl[i][j + 1], dp_br_tl[i + 1][j]) + costarr[i][j]


dp_bl_tr[n - 1][0] = costarr[n - 1][0]
for i in range(1, m):
    dp_bl_tr[n - 1][i] = dp_bl_tr[n - 1][i - 1] + costarr[n - 1][i]
for i in range(n - 2, -1, -1):
    dp_bl_tr[i][0] = dp_bl_tr[i + 1][0] + costarr[i][0]
for i in range(n - 2, -1, -1):
    for j in range(1, m):
        dp_bl_tr[i][j] = max(dp_bl_tr[i][j - 1], dp_bl_tr[i + 1][j]) + costarr[i][j]


dp_tr_bl[0][m - 1] = costarr[0][m - 1]
for i in range(m - 2, -1, -1):
    dp_tr_bl[0][i] = dp_tr_bl[0][i + 1] + costarr[0][i]
for i in range(1, n):
    dp_tr_bl[i][m - 1] = dp_tr_bl[i - 1][m - 1] + costarr[i][m - 1]
for i in range(1, n):
    for j in range(m - 2, -1, -1):
        dp_tr_bl[i][j] = max(dp_tr_bl[i][j + 1], dp_tr_bl[i - 1][j]) + costarr[i][j]


def sh(arr):
    for i in arr:
        print(i)


ans = 0

for i in range(1, n - 1):
    for j in range(1, m - 1):
        ans = max(ans, dp_bl_tr[i][j - 1] + dp_tr_bl[i][j + 1] + dp_tl_br[i - 1][j] + dp_br_tl[i + 1][j])
        ans = max(ans, dp_bl_tr[i + 1][j] + dp_tr_bl[i - 1][j] + dp_tl_br[i][j - 1] + dp_br_tl[i][j + 1])

stdout.write(str(ans) + "\n")
