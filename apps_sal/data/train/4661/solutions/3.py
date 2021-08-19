def pattern(n):
    digits = ''.join((str(i % 10) for i in range(1, n + 1)))
    spaces = ' ' * (n - 1)
    return '\n'.join(('{}{}{}'.format(spaces[i:], digits, spaces[:i]) for i in range(n)))
