def solve(st, idx):
    if st[idx] != '(':
        return -1
    key = 1
    for (n, letter) in enumerate(st[idx + 1:]):
        if key == 0:
            return idx + n
        if letter == ')':
            key -= 1
        elif letter == '(':
            key += 1
    if key == 0:
        return idx + n + 1
    return -1
