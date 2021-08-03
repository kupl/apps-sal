def est_subsets(arr):
    s = set(arr)
    n = (2 ** len(s)) - 1
    return n   # n: amount of subsets that do not have repeated elements
