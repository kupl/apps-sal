def find_spec_partition(n, k, com):
    if com == 'min':
        return [n - k + 1] + [1] * (k-1)
    q, r = divmod(n, k)
    return [q+1] * r + [q] * (k-r)
