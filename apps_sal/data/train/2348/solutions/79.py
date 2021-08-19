import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
X = [int(a) for a in input().split()]
L = int(input())
NE = []
j = 0
for (i, x) in enumerate(X):
    while j < N - 1 and X[j + 1] <= x + L:
        j += 1
    NE.append(j)
D = [NE[:]]
for _ in range(16):
    d = D[-1]
    nd = [d[dd] for dd in d]
    D.append(nd)
Q = int(input())
for _ in range(Q):
    (a, b) = map(int, input().split())
    (a, b) = (a - 1, b - 1)
    if a > b:
        (a, b) = (b, a)
    re = 0
    s = a
    for i in range(17)[::-1]:
        d = D[i]
        if d[s] < b:
            s = d[s]
            re += 1 << i
    print(re + 1)
