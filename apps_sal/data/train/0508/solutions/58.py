import sys
from heapq import heapify, heappop, heappush


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, Q = lr()
STX = [tuple(lr()) for _ in range(N)]
event = []
append = event.append
for s, t, x in STX:
    append((s - x, 0, x))
    append((t - x, -1, x))

for i in range(Q):
    d = ir()
    append((d, 1, i))

event.sort()
answer = [-1] * Q
cur = set()
flag = False
INF = 10 ** 10
min_x = INF
add = cur.add
remove = cur.remove
for a, b, c in event:
    if b == 0:
        add(c)
        if c < min_x:
            min_x = c
            flag = True
    elif b == -1:
        remove(c)
        if min_x == c:
            flag = False
    elif b == 1:
        if cur:
            if not flag:
                min_x = min(cur)
                flag = True
            answer[c] = min_x

print(('\n'.join(map(str, answer))))
