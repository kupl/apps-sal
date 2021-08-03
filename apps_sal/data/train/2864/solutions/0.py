def merge_arrays(a, b):
    out = []
    for n in a + b:
        if n in a and n in b:
            if a.count(n) == b.count(n):
                out.append(n)
        else:
            out.append(n)
    return sorted(set(out))
