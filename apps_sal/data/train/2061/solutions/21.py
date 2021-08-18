
"""

算数
かなり嫌

三角形をパタパタした場合の最短距離
重心で考える
と、かなり変な形

とりあえず定式化する

(0,0) スタート

axay…をこれに落とし込みたい

0  11  22  3
00 1    2 33

ans から減らす

10
1 1 1 2 2 1

が3になる必要性

"""

import sys
from sys import stdin

TT = int(stdin.readline())

t0 = tuple(sorted([(0, 0), (0, 1), (1, 0)]))
t1 = tuple(sorted([(0, 0), (0, 1), (1, 1)]))
t2 = tuple(sorted([(0, 1), (1, 0), (1, 1)]))
t3 = tuple(sorted([(0, 0), (1, 0), (1, 1)]))

for loop in range(TT):

    ax, ay, bx, by, cx, cy = list(map(int, stdin.readline().split()))

    mx = min(ax, bx, cx)
    my = min(ay, by, cy)

    ox = 2 * mx
    oy = 2 * my

    setz = tuple(sorted([(ax - mx, ay - my), (bx - mx, by - my), (cx - mx, cy - my)]))

    if setz == t0:
        ox += 0
        oy += 0
    elif setz == t1:
        ox += 0
        oy += 1
    elif setz == t2:
        ox += 1
        oy += 1
    else:
        ox += 1
        oy += 0

    if ox != oy:
        print((abs(ox) + abs(oy) - min(abs(ox), abs(oy))))
    else:

        if 0 <= ox <= 1:
            print(ox)
        else:
            print((abs(ox) + abs(oy) - min(abs(ox), abs(oy)) + 1))
