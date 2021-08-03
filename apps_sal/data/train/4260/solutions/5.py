def mark_spot(n):
    if not type(n) == int or n < 1 or not n % 2:
        return '?'

    l = [' ' * (2 * n - i * 2) for i in range(n // 2 + 1)]

    for i in range(len(l)):
        l[i] = l[i][:-2] + 'X' + '\n'
        l[i] = ' ' * i * 2 + 'X' + l[i][i * 2 + 1:]

    return ''.join(l + l[::-1][1:])
