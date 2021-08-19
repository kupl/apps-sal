def advice(agents, n):
    A = {(i, j) for (i, j) in agents if 0 <= i < n and 0 <= j < n}
    B = {(i, j) for i in range(n) for j in range(n)}
    if A == B:
        return []
    while len(A) > 0 and A != B:
        B = B - A
        A = {(i, j) for (i, j) in B if (i + 1, j) in A or (i - 1, j) in A or (i, j + 1) in A or ((i, j - 1) in A)}
    return sorted(list(B))
