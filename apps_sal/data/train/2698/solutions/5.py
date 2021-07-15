def sum_arrays(A, B):
    if A == B == [0]: return []
    if not (A and B): return A or B
    S = sum(int(''.join(map(str, arr))) for arr in (A, B))
    res = [int(d) for d in str(abs(S))]
    return [-res[0] if S < 0 else res[0]] + res[1:]
