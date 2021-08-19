def number(lines):
    for (index, char) in enumerate(lines):
        lines[index] = f'{index + 1}: {char}'
    return lines
