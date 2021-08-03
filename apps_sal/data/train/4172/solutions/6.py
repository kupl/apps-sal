def solve(s):
    if len(s) & 1:
        return -1
    inv = open = 0
    for c in s:
        if c == '(':
            open += 1
        elif open:
            open -= 1
        else:
            open = 1
            inv += 1
    return inv + open // 2
