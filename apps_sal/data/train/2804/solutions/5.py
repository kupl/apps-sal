def custom_christmas_tree(chars, n):
    trunc = n // 3
    string = ''
    l, i = len(chars), 0
    for r in range(n):
        string += ' ' * (n - r - 1)
        for c in range(r + 1):
            string += chars[i % l]
            string += ' ' if c < r else '\n'
            i += 1
    for r in range(trunc):
        string += ' ' * (n - 1) + '|'
        string += '\n' if r < trunc - 1 else ''
    return string
