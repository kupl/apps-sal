def array_operations(A, k, p=0, q=0):
    (D, E) = ({}, {})
    for i in range(k):
        s = str(A)
        if s in D:
            A = D[s]
            p = i
            q = E[s]
            break
        m = max(A)
        A = [m - a for a in A]
        D[s] = A
        E[s] = i
    if p != q:
        for i in range(q + (k - q) % (p - q)):
            A = D[str(A)]
    return A
