def fold_to(B):
    if B < 0: return None
    B *= 10_000
    L = 1
    M = 0
    while L < B:
        L *= 2
        M += 1
    return M
        

