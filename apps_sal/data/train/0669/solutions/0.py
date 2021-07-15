T = int(input())
for _ in range(T):
    N, M, K = [int(x) for x in input().split()]
    UV = [[int(x) for x in input().split()] for _ in range(M)]
    Q = int(input())
    AB = [[int(x) for x in input().split()] for _ in range(Q)]
 
    X = [[i] for i in range(N)]
    for u, v in UV:
     X[u - 1] += [v - 1]
     X[v - 1] += [u - 1]
 
    A = [[1 if i > 0 or j == 0 else 0 for j in range(N)] for i in range(K + 1)]
    for a, b in AB:
     A[b] = [1 if i == a - 1 else 0 for i in range(N)]
 
    if A[0][0] == 1:
     for k in range(K - 1, -1, -1):
      for i in range(N):
       if A[k][i] != 0:
        A[k][i] = sum(A[k + 1][j] for j in X[i])
 
    print(A[0][0])
