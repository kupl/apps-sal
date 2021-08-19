def hollow_triangle(n):
    return [''.join([['_', '#'][k in [n - 1 - i, n - 1 + i]] for k in range(n * 2 - 1)]) for i in range(n - 1)] + [f"{'#' * (n * 2 - 1)}"]
