def number(lines):
    lines = [f'{str(i + 1)}: {lines[i]}' for i in range(len(lines))]
    return lines
