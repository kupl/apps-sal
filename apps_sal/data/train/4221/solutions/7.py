def count_targets(n, a):
    return sum(a[i] == a[i-n] for i in range(n, len(a)))
