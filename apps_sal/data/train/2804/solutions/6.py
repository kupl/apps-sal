def custom_christmas_tree(chars, n):
    chars *= n * n

    def s(n):
        return (n + 1) * n // 2

    def pad(s):
        return ' ' * (n - len(s) // 2 - 1) + s

    def row(i):
        return pad(' '.join(chars[s(i):s(i) + i + 1]))
    return '\n'.join([*map(row, range(n))] + [pad('|')] * (n // 3))
