def subsets_parity(n, k):
    N, K = bin(n)[2:][::-1], bin(k)[2:][::-1]
    for i in range(len(K)):
        if K[i] > N[i]:
            return 'EVEN'
    return 'ODD'
