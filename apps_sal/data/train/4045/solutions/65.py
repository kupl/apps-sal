def number(lines):
    if not lines: return []
    return [f'{x}: {y}' for x,y in enumerate(lines, 1)]
