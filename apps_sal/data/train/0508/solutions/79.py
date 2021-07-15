import heapq
import sys
input = sys.stdin.readline

N, Q = (int(i) for i in input().split())
L = [0] * 2 * N
for i in range(N):
    S, T, X = (int(i) for i in input().split())
    L[2 * i] = (S-X, X, 1)
    L[2 * i + 1] = (T-X, X, 0)

L.sort(reverse=True)

Xs = set([])
XH = []
heapq.heapify(XH)
for i in range(Q):
    D = int(input())
    ans = 0
    while True:
        if L:
            t, X, f = L.pop()
            if t <= D:
                if f == 1:
                    Xs.add(X)
                    heapq.heappush(XH, X)
                else:
                    Xs.remove(X)
            else:
                L.append((t, X, f))
                break
        else:
            break
    if Xs:
        while XH[0] not in Xs:
            X = heapq.heappop(XH)
        print(XH[0])
    else:
        print("-1")
