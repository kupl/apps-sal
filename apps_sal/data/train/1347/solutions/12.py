(n, m) = input().split()
K = list(map(int, input().split()))
L = []
M = []
for i in range(int(m)):
    (a, b, c) = input().split()
    if int(a) in K:
        M.append([int(b), c])
    else:
        L.append([int(b), c])
M.sort()
M.reverse()
L.sort()
L.reverse()
for i in range(len(M)):
    print(M[i][1])
for i in range(len(L)):
    print(L[i][1])
