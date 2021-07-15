def number(lines):
    return list('%d: %s' % (n, s) for (n, s) in enumerate(lines, 1))
