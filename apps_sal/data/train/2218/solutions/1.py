import sys
input = sys.stdin.readline

from bisect import bisect_left as bl

N = int(input())
A = [int(a) for a in input().split()]
Q = int(input())
L = [-1] * N

X = []
Y = []

for i in range(Q):
    t = [int(a) for a in input().split()]
    if t[0] == 1:
        p, x = t[1]-1, t[2]
        A[p] = x
        L[p] = i
    else:
        x = t[1]
        while len(Y) and Y[-1] <= x:
            X.pop()
            Y.pop()
        X.append(i)
        Y.append(x)
    
for i in range(N):
    j = bl(X, L[i])
    if j < len(X):
        A[i] = max(A[i], Y[j])

print(*A)


