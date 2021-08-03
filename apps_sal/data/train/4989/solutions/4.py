def hollow_triangle(n):
    return ['_' * (n - i - 1) + '#' + '_' * (2 * i - 1) + '#' * (i >= 1) + '_' * (n - i - 1)
            for i in range(n - 1)] + ['#' * (2 * n - 1)]
