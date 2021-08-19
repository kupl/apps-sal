import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    N = int(input())
    A = [int(a) for a in input().split()]
    X = {}
    for a in A:
        if a in X:
            X[a] += 1
        else:
            X[a] = 1
    Y = []
    for x in X:
        Y.append(X[x])
    Y = sorted(Y)[::-1]
    prev = Y[0] + 1
    su = 0
    for i in range(len(Y)):
        ne = min(prev - 1, Y[i])
        if ne <= 0:
            break
        su += ne
        prev = ne
    print(su)
