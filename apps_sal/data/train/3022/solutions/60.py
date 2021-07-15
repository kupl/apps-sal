def two_highest(arg1):
    out = []
    for v in sorted(arg1, reverse=True):
        if len(out) == 2:
            break
        if v not in out:
            out.append(v)
    return out
