def solve(st, idx):
    if st[idx] != "(":
        return -1

    open_par = 0
    for i, ch in enumerate(st[idx + 1:]):
        if ch == "(":
            open_par += 1
        elif ch == ")":
            if not open_par:
                return i + idx + 1
            open_par -= 1
