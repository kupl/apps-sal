def number(lines):
    return list(map(lambda x, y: str(y) + ': ' + x, lines, range(1, len(lines) + 1)))
