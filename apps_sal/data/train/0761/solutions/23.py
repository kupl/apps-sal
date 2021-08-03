t = int(input())
for i in range(t):
    inp1 = str(input()).split()
    N = int(inp1[0])
    K = int(inp1[1])
    M = int(inp1[2])
    A = str(input()).split()
    B = str(input()).split()
    C = str(input()).split()
    D = str(input()).split()
    R = [0] * N
    arr = [0] * (K + M)
    for j in range(K):
        arr[j] = int(C[j])
    for j in range(M):
        arr[j + K] = int(D[j])
    arr.sort()
    arr = arr[::-1]
    for j in range(N):
        R[j] = int(A[j]) - int(B[j])
    R.sort()
    R = R[::-1]
    ii = 0
    fl = 0
    for j in range(N):
        while(1):
            if ii >= K + M:
                fl = 1
                break
            if arr[ii] <= R[j]:
                break
            else:
                ii += 1
        if fl == 1:
            break
        R[j] -= arr[ii]
        ii += 1
    su = sum(R)
    print(su)
