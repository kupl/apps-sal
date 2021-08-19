def number(lines):
    if not lines:
        return []
    else:
        return ['%s: %s' % (str(i), str(j)) for (i, j) in enumerate(lines, start=1)]
