def mark_spot(n):
    if not isinstance(n, int) or not n % 2 or n < 1:
        return '?'

    spots = [[' '] * n for _ in range(n)]
    for i, row in enumerate(spots):
        row[i], row[-1 - i] = 'XX'

    return '\n'.join(' '.join(row).rstrip() for row in spots + [""])
