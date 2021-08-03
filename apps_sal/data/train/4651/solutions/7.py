def christmas_tree(height):
    s = '* *** *****'.split()
    r = []
    for i in range(height // 3):
        for x in s:
            r.append(' ' * ((2 * (height // 3) + 3 - 2 * i - len(x)) // 2) + '*' * 2 * i + x)
    return '\r\n'.join(r + [' ' * (height // 3) + '###']) if height // 3 else ''
