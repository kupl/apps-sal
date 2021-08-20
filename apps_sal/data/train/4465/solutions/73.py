def super_size(n):
    n_str = str(n)
    n_sorted = sorted(n_str, reverse=True)
    res = int(''.join(n_sorted))
    return res
