def interleave(*args):
    n_max = len(max(args, key=len))
    return [j[i] if i < len(j) else None for i in range(n_max) for j in args]
