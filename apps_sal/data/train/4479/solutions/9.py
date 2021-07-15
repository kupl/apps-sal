def elements_sum(arr, d=0):
    return sum([x[len(arr) - 1 - i] if len(arr) - 1 - i < len(x) else d for (i, x) in enumerate(arr)])
