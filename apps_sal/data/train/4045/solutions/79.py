def number(lines):
    if len(lines) > 0:
        for i in range(0, len(lines)):
            lines[i] = f'{i + 1}: {lines[i]}'
    return lines
