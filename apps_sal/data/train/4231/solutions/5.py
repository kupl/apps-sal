def a(n):
    return '\n'.join(['A'.center(2 * (n - (n & 1)) - 1)] + [[('A ' * ((n - (n & 1)) // 2 + 1)).rstrip().center(2 * (n - (n & 1)) - 1), ('A' + ' ' * (i * 2 + 1) + 'A').center(2 * (n - (n & 1)) - 1)][i != (n - (n & 1)) // 2 - 1] for i in range(n - 1 - (n & 1))]) if n - (n & 1) > 3 else ''
