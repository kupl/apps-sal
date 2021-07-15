import sys
input = sys.stdin.readline
from operator import itemgetter

X, Y, N = map(int, input().split())
U = []
D = []
R = []
L = []

def mustconsider(x, y):
    return (x in [0, X]) or (y in [0, Y])

def divide(x, y, i):
    if x == 0 and y != Y:
        L.append((y, i))
    if x == X and y != 0:
        R.append((y, i))
    if y == 0 and x != 0:
        D.append((x, i))
    if y == Y and x != X:
        U.append((x, i))

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if mustconsider(x1, y1) and mustconsider(x2, y2):
        divide(x1, y1, i)
        divide(x2, y2, i)

D.sort()
R.sort()
U.sort(reverse=True)
L.sort(reverse=True)

Arounds = []
for _, ind in D:
    Arounds.append(ind)
for _, ind in R:
    Arounds.append(ind)
for _, ind in U:
    Arounds.append(ind)
for _, ind in L:
    Arounds.append(ind)

stack = []
for a in Arounds:
    if not stack:
        stack.append(a)
    else:
        if stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)

print("YES" if not stack else "NO")
