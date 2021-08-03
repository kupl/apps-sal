from math import ceil


def union_jack(size):
    if isinstance(size, int) or isinstance(size, float):
        n = max(ceil(float(size)), 7)
    else:
        return False
    jack = []
    for i in range(n):
        row = ['-'] * n
        row[(n - 1 + (not n % 2)) // 2] = row[(n - 1) // 2] = row[i] = row[n - 1 - i] = 'X'
        jack.append(''.join(row))
    jack[(n - 1) // 2] = jack[(n - 1 + (not n % 2)) // 2] = 'X' * n
    return '\n'.join(jack)
