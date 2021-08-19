def find_dups_miss(arr):
    a = sorted(arr)
    return [sum(range(a[0], a[-1] + 1)) - sum(set(a)), sorted(set(a[::2]) & set(a[1::2]))]
