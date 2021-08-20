def number(lines):
    return ['{}: {}'.format(*line) for line in enumerate(lines, start=1)]
