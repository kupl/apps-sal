def number(lines):
    return ['%s: %s' % (n, lines[n - 1]) for n in range(1, len(lines) + 1)] if lines else lines
