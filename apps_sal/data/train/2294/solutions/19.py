# seishin.py
from heapq import heappush, heappop, heapify

N = int(input())
P = []
for i in range(N):
    x, y = map(int, input().split())
    P.append((x, y) if x < y else (y, x))

X = [x for x, y in P]
Y = [y for x, y in P]

MIN = min(X)
MAX = max(Y)

# R_min = MIN, B_max = MAX
res = (max(X) - MIN) * (MAX - min(Y))

# R_min = MIN, R_max = MAX
base = MAX - MIN
heapify(P)

# 出来る限りスライドさせながら(B_max - B_min)を最小化
r = max(X)
while P:
    x, y = heappop(P)
    res = min(res, base * (r - x))
    if y != -1:
        # Bに入ってたxをRに入れて代わりにyをBに入れる
        heappush(P, (y, -1))
        r = max(r, y)
    else:
        # (x, y) のyの方がB_minに該当
        # => これ以上B_minを落とせない
        break

print(res)
