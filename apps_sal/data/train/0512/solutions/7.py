from collections import deque
import sys
input = sys.stdin.readline

N, Q = list(map(int, input().split()))
EDGE = [list(map(int, input().split())) for i in range(N - 1)]
Query = [list(map(int, input().split())) for i in range(Q)]
mod = 10**9 + 7

EDGELIST = [dict() for i in range(N + 1)]
for x, y, c, l in EDGE:
    EDGELIST[x][y] = (c, l)
    EDGELIST[y][x] = (c, l)

# LCA(オイラーツアー＋Segment tree)

DEPTH = [-1] * (N + 1)
DEPTH[1] = 0

QUE = deque([1])
QUE2 = deque()
EULER = []  # (i,j)で,(1からツアーで辿った点の深さ,そのindex)

USED = [0] * (N + 1)
while QUE:
    x = QUE.pop()
    EULER.append((DEPTH[x], x))
    if USED[x] == 1:
        continue
    for to in EDGELIST[x]:

        if USED[to] == 0:
            DEPTH[to] = DEPTH[x] + 1
            QUE2.append(to)
        else:
            QUE.append(to)
    QUE.extend(QUE2)
    QUE2 = deque()

    USED[x] = 1

MINP = [1 << 30] * (N + 1)
MAXP = [-1] * (N + 1)

for ind, (depth, p) in enumerate(EULER):
    MINP[p] = min(MINP[p], ind)
    MAXP[p] = ind

LEN = len(EULER)

seg_el = 1 << (LEN.bit_length())  # Segment treeの台の要素数
SEG = [(1 << 30, 0)] * (2 * seg_el)  # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(LEN):  # Dを対応する箇所へupdate
    SEG[i + seg_el] = EULER[i]

for i in range(seg_el - 1, 0, -1):  # 親の部分もupdate
    SEG[i] = min(SEG[i * 2], SEG[i * 2 + 1])


def update(n, x, seg_el):  # A[n]をxへ更新（反映）
    i = n + seg_el
    SEG[i] = x
    i >>= 1  # 子ノードへ

    while i != 0:
        SEG[i] = min(SEG[i * 2], SEG[i * 2 + 1])
        i >>= 1


def getvalues(l, r):  # 区間[l,r)に関するminを調べる
    L = l + seg_el
    R = r + seg_el
    ANS = (1 << 30, 0)

    while L < R:
        if L & 1:
            ANS = min(ANS, SEG[L])
            L += 1

        if R & 1:
            R -= 1
            ANS = min(ANS, SEG[R])
        L >>= 1
        R >>= 1

    return ANS


def LCA(l, r):
    return getvalues(min(MINP[l], MINP[r]), max(MAXP[l], MAXP[r]) + 1)


N_q = [[] for i in range(N + 1)]
for ind, (c, pl, x, y) in enumerate(Query):
    N_q[x].append([ind, c, pl, 1])
    N_q[y].append([ind, c, pl, 1])
    N_q[LCA(x, y)[1]].append([ind, c, pl, 0])

ANS = [0] * Q

LENG = 0
C_LENGTH = [0] * N
C_SUM = [0] * N

for i in range(1, len(EULER)):
    ind = EULER[i][1]
    c, l = EDGELIST[EULER[i - 1][1]][ind]
    if EULER[i][0] > EULER[i - 1][0]:
        LENG += l
        C_LENGTH[c] += l
        C_SUM[c] += 1

        for que, c, pl, boo in N_q[ind]:
            if boo == 1:
                ANS[que] += LENG + C_SUM[c] * pl - C_LENGTH[c]

            else:
                ANS[que] -= (LENG + C_SUM[c] * pl - C_LENGTH[c]) * 2

    else:
        LENG -= l
        C_LENGTH[c] -= l
        C_SUM[c] -= 1

for ans in ANS:
    print(ans)
