
N = input()
A = input()
N = N.split()
A = A.split()
N = list(map(int, N))
A = list(map(int, A))
MAX = max(A)
MIN = min(A)
if N[1] == 0:
    for i in range(N[0]):
        print(A[i], end=' ')
else:
    if N[1] % 2 == 1:
        for i in range(N[0]):
            A[i] = MAX - A[i]
            print(A[i], end=' ')
    else:
        for i in range(N[0]):
            A[i] = A[i] - MIN
            print(A[i], end=' ')
