def solve(st, idx):
    if st[idx] != '(':
        return -1
    open = 1
    for i in range(idx+1, len(st)):
        if st[i] == '(':
            open += 1
        elif st[i] == ')':
            open -= 1
        if open == 0:
            return i
