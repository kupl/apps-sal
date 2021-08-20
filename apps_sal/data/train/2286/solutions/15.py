(K, N) = map(int, input().split())
if K % 2 == 0:
    print(K // 2, end=' ')
    for i in range(1, N):
        if i != N - 1:
            print(K, end=' ')
        else:
            print(K)
else:

    def superlist(L, n):
        if n % 2 == 1:
            return [L // 2 + 1] + superlist(L, n - 1)
        else:
            Ax = [L // 2 + 1 for i in range(n)]
            j = n - 1
            for i in range(n // 2):
                Ax[j] -= 1
                if Ax[j] == 0:
                    j -= 1
                else:
                    for m in range(j + 1, n):
                        Ax[m] = L
                    j = n - 1
            return Ax
    if K == 1:
        for i in range((N - 1) // 2 + 1):
            if i != (N - 1) // 2:
                print(1, end=' ')
            else:
                print(1)
    else:
        A = superlist(K, N)
        for _ in range(N):
            if _ != N - 1 and A[_] != 0:
                print(A[_], end=' ')
            elif _ == N - 1 and A[_] != 0:
                print(A[_])
