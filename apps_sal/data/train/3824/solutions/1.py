def find_spec_partition(n, k, com):
    return [n - k + 1] + [1] * (k - 1) if com == "min" else [n // k + 1] * (n % k) + [n // k] * (k - n % k)
