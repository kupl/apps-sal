import sys
from collections import deque
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))


R, C, N = MI()
A1, A2, A3, A4 = [], [], [], []


def f(x, y):  # (x,y)が周上にあるか判定
    if x == 0 or x == R or y == 0 or y == C:
        return True
    return False


for i in range(1, N + 1):
    x1, y1, x2, y2 = MI()
    if not (f(x1, y1) and f(x2, y2)):
        continue
    if y1 == 0:
        A1.append((x1, i))
    elif y1 == C:
        A3.append((-x1, i))
    elif x1 == 0:
        A4.append((-y1, i))
    else:
        A2.append((y1, i))
    if y2 == 0:
        A1.append((x2, i))
    elif y2 == C:
        A3.append((-x2, i))
    elif x2 == 0:
        A4.append((-y2, i))
    else:
        A2.append((y2, i))

A1.sort()
A2.sort()
A3.sort()
A4.sort()
A = A1 + A2 + A3 + A4

deq = deque([])
flag = [0] * (N + 1)
for z, i in A:
    if flag[i] == 0:
        flag[i] = 1
        deq.append(i)
    else:
        j = deq.pop()
        if j != i:
            print('NO')
            return
else:
    print('YES')
