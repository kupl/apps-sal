def solve(s):
    clean = "".join([str(c) if c.isdigit() else " " for c in s])
    return max(list([int(x) for x in list([_f for _f in clean.split(" ") if _f])]))
