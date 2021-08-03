import sys
def input(): return sys.stdin.readline().rstrip()


def calc(a, b):
    if b == 0:
        return a
    if a == R:
        return b + R
    if b == C:
        return R + C + (R - a)
    if a == 0:
        return R + C + R + (C - b)


R, C, N = map(int, input().split())
A = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 == 0 or x1 == R or y1 == 0 or y1 == C) and (x2 == 0 or x2 == R or y2 == 0 or y2 == C):
        A.append((calc(x1, y1), i))
        A.append((calc(x2, y2), i))

A = [l[1] for l in sorted(A, key=lambda x: x[0])]
B = []

while A:
    while len(B) and A[-1] == B[-1]:
        A.pop()
        B.pop()
    if A:
        B.append(A.pop())

print("NO" if len(B) else "YES")
