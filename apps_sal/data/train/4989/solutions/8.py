def hollow_triangle(n):
    lines = ['_' * (n-i-1) + '#' + '_' * (2*i-1) + '#' + '_' * (n-i-1) for i in range(1, n-1)]
    return ['_' * (n-1) + '#' + '_' * (n-1)] + lines + ['#' * (2*n-1)] if n > 1 else ['#']
