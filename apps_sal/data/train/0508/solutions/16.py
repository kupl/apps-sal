import heapq
import sys
input = sys.stdin.readline
(N, Q) = (int(i) for i in input().split())
L = [0] * (2 * N + Q)
for i in range(N):
    (S, T, X) = (int(i) for i in input().split())
    L[2 * i] = (S - X, 1, X)
    L[2 * i + 1] = (T - X, -1, X)
for i in range(Q):
    D = int(input())
    L[2 * N + i] = (D, 2, 0)
L.sort()
Xs = set([])
XH = []
heapq.heapify(XH)
for (t, f, X) in L:
    if f == 1:
        Xs.add(X)
        heapq.heappush(XH, X)
    elif f == -1:
        Xs.remove(X)
    elif Xs:
        while XH[0] not in Xs:
            X = heapq.heappop(XH)
        print(XH[0])
    else:
        print('-1')
