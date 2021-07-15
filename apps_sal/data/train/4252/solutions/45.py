def merge_arrays(first, second):
    M = list(set(first + second))
    M.sort()
    return M
