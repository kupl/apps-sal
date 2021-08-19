def diamond(n):
    return ''.join([('*' * k).center(n).rstrip() + '\n' for k in range(1, n + 1, 2)] + [(' *' * k).center(n).rstrip() + '\n' for k in range(n - 2, 0, -2)]) if n > 0 and n % 2 == 1 else None
