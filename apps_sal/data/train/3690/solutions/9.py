def solve(st, idx):
    length = len(st)
    opened = 0
    start = st[idx]
    if start != '(':
        return -1
    for i in range(idx, length, 1):
        if st[i] == ')':
            if opened != 0:
                opened = opened - 1
            if opened == 0:
                return i
        elif st[i] == '(':
            opened = opened + 1
    return -1
