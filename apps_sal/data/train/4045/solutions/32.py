def number(lines):
    return ['{0}: {1}'.format(x + 1, lines[x]) for x in range(len(lines))]
