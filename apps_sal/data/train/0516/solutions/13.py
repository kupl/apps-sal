for T in range(int(input())):
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    C = [0, 0]
    for Z in range(2):
        L = N * (Z + 1)
        A *= Z + 1
        for I in range(L - 1):
            for J in range(I + 1, L):
                if A[I] > A[J]:
                    C[Z] += 1
    print(C[0] + (K - 1) * (C[1] + (K - 1) * (C[1] - 2 * C[0])) // 2)
