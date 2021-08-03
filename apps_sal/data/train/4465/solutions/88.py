def super_size(n):
    L = [int(i) for i in str(n)]
    L.sort(reverse=True)
    S = [str(i) for i in L]
    A = "".join(S)
    return int(A)
