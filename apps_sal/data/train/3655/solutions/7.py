def my_crib(n):
    return '\n'.join([('/' + [' ', '_'][i == n] * (i * 2) + '\\').center(n * 2 + 2, ' ') for i in range(n + 1)]) + '\n' + '\n'.join(['|' + [' ', '_'][i == n - 1] * (n * 2) + '|' for i in range(n)])
