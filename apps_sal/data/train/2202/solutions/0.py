import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
BIT = [0] * (n + 1)


def update(v, w):
    while v <= n:
        BIT[v] += w
        v += v & -v


def getvalue(v):
    ANS = 0
    while v != 0:
        ANS += BIT[v]
        v -= v & -v
    return ANS


for i in range(1, n + 1):
    update(i, i)
ANS = [-1] * n
for i in range(n - 1, -1, -1):
    MIN = 0
    MAX = n
    k = A[i]
    while True:
        x = (MIN + MAX + 1) // 2
        if getvalue(x) > k:
            if getvalue(x - 1) == k:
                ANS[i] = x
                break
            else:
                MAX = x
        else:
            MIN = x
    update(x, -x)
print(*ANS)
