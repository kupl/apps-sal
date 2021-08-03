def Z_algorithm(S):
    l = len(S)
    A = [0] * l
    A[0] = l
    i = 1
    j = 0
    while i < l:
        while i + j < l and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l - i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A


def jugde(W):
    Z = Z_algorithm(W)
    l = len(W)
    B = [True] * l
    for p in range(1, l):
        if not B[p - 1]:
            continue
        k = 2
        while (k - 1) * p <= Z[p]:
            B[k * p - 1] = False
            k += 1
    return B


def solve(W):
    n = len(W)
    if len(set(W)) == 1:
        print(n)
        print(1)
        return
    G = jugde(W)
    W.reverse()
    G_rev = jugde(W)
    if G[-1]:
        print(1)
        print(1)
        return
    print(2)
    cnt = 0
    for i in range(n - 1):
        cnt += G[i] and G_rev[-(i + 2)]
    print(cnt)
    return


solve(list(input()))
