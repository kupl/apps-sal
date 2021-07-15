def xMasTree(n):
    width = 2 * n - 1
    return [
        ('#' * (m if m <= width else 1)).center(width, '_')
        for m in range(1, width + 5, 2)]
