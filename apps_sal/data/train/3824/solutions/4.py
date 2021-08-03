def find_spec_partition(n, k, com):
    if com == 'min':
        return [n - k + 1] + [1] * (k - 1)
    else:
        return [(n // k + 1 if i < n % k else n // k) for i in range(k)]
    return r
