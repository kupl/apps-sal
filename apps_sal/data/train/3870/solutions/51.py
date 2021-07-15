def solve(s):
    spc_idx = []
    rs = ''
    for i,c in enumerate(s):
        if c == ' ':
            spc_idx.append(i)
        else:
            rs = c + rs
    for i in spc_idx:
        rs = rs[:i] + ' ' + rs[i:]
    return rs
