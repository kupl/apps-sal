def solve(st, idx):
    if st[idx] != "(": return -1
    d = 1
    while d > 0:
        idx += 1
        if st[idx] == ")": d -= 1
        if st[idx] == "(": d += 1    
    return idx
