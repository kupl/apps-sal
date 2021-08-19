def xMasTree(n):
    w = list(range(1, n * 2, 2)) + [1, 1]
    return [f"{'#' * i}".center(n * 2 - 1, '_') for i in w]
