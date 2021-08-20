def number(lines):
    return list((f'{no}: {line}' for (no, line) in enumerate(lines, 1)))
