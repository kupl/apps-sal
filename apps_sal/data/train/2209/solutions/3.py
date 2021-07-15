import sys

n = int(sys.stdin.readline().strip())
N = [[] for i in range (0, n)]
C = [-1 for i in range (0, n)]
for i in range (0, n-1):
    a, b = list(map(int,sys.stdin.readline().strip().split()))
    a, b = a-1, b-1
    N[a].append(b)
    N[b].append(a)
C[0] = 0
L0 = [0]
L1 = []
while len(L0) + len(L1) > 0:
    for i in L0:
        for j in N[i]:
            if C[j] == -1:
                C[j] = 1
                L1.append(j)
    L0 = []
    for i in L1:
        for j in N[i]:
            if C[j] == -1:
                C[j] = 0
                L0.append(j)
    L1 = []
f = 1
F = n-1
L = []
M = []
for i in range (0, n):
    if len(N[i]) == 1:
        L.append(N[i])
        M.append(i)
L.sort()
for i in range (0, len(L)-1):
    if L[i] == L[i+1]:
        F = F - 1
    if C[M[i]] != C[M[i+1]]:
        f = 3
print(f, F)
