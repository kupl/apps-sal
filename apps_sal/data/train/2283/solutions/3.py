from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    (N, a, b, da, db) = list(map(int, input().split()))
    (a, b) = (a - 1, b - 1)
    X = [[] for _ in range(N)]
    Y = [[] for _ in range(N)]
    for _ in range(N - 1):
        (u, v) = list(map(int, input().split()))
        X[u - 1].append(v - 1)
        X[v - 1].append(u - 1)
        Y[u - 1].append(v - 1)
        Y[v - 1].append(u - 1)
    if 2 * da >= db:
        print('Alice')
        continue
    P = [-1] * N
    Q = deque([a])
    R = []
    D = [0] * N
    while Q:
        i = deque.popleft(Q)
        R.append(i)
        for j in X[i]:
            if j != P[i]:
                P[j] = i
                D[j] = D[i] + 1
                X[j].remove(i)
                deque.append(Q, j)
    if D[b] <= da:
        print('Alice')
        continue
    ma = max(D)
    for i in range(N):
        if D[i] == ma:
            break
    X = Y
    P = [-1] * N
    Q = deque([i])
    R = []
    D = [0] * N
    while Q:
        i = deque.popleft(Q)
        R.append(i)
        for j in X[i]:
            if j != P[i]:
                P[j] = i
                D[j] = D[i] + 1
                X[j].remove(i)
                deque.append(Q, j)
    print('Bob' if max(D) > 2 * da else 'Alice')
