def mark_spot(n):
    return '?' if not isinstance(n, int) or n < 1 or n % 2 == 0 else '\n'.join(('{0}{1}{0}'.format('X' if i != n // 2 else '', ' ' * (abs(n - 1 - 2 * i) * 2 - 1) if i != n // 2 else 'X').center(n * 2).rstrip() for i in range(n))) + '\n'
